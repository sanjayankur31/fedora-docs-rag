&#42; Programming Languages :experimental: :toc:

# The C Programming Language {#_the_c_programming_language}

## The Core Language {#sect-Defensive_Coding-C-Language}

C provides no memory safety. Most recommendations in this section deal
with this aspect of the language.

### Undefined Behavior {#sect-Defensive_Coding-C-Undefined}

Some C constructs are defined to be undefined by the C standard. This
does not only mean that the standard does not describe what happens when
the construct is executed. It also allows optimizing compilers such as
GCC to assume that this particular construct is never reached. In some
cases, this has caused GCC to optimize security checks away. (This is
not a flaw in GCC or the C language. But C certainly has some areas
which are more difficult to use than others.)

Common sources of undefined behavior are:

&#42; out-of-bounds array accesses

&#42; null pointer dereferences

&#42; overflow in signed integer arithmetic

### Recommendations for Pointers and Array Handling {#sect-Defensive_Coding-C-Pointers}

Always keep track of the size of the array you are working with. Often,
code is more obviously correct when you keep a pointer past the last
element of the array, and calculate the number of remaining elements by
subtracting the current position from that pointer. The alternative,
updating a separate variable every time when the position is advanced,
is usually less obviously correct.

&lt;&lt;ex-Defensive_Coding-C-Pointers-remaining&gt;&gt; shows how to
extract Pascal-style strings from a character buffer. The two pointers
kept for length checks are &#96;inend&#96; and &#96;outend&#96;.
&#96;inp&#96; and &#96;outp&#96; are the respective positions. The
number of input bytes is checked using the expression &#96;len &gt;
(size_t)(inend - inp)&#96;. The cast silences a compiler warning;
&#96;inend&#96; is always larger than &#96;inp&#96;.

:::: {#ex-Defensive_Coding-C-Pointers-remaining .example}
::: title
Array processing in C
:::

``` c
```
::::

It is important that the length checks always have the form &#96;len
&gt; (size_t)(inend - inp)&#96;, where &#96;len&#96; is a variable of
type &#96;size_t&#96; which denotes the &#42;total&#42; number of bytes
which are about to be read or written next. In general, it is not safe
to fold multiple such checks into one, as in &#96;len1 + len2 &gt;
(size_t)(inend - inp)&#96;, because the expression on the left can
overflow or wrap around (see
&lt;&lt;sect-Defensive_Coding-C-Arithmetic&gt;&gt;), and it no longer
reflects the number of bytes to be processed.

### Recommendations for Integer Arithmetic {#sect-Defensive_Coding-C-Arithmetic}

Overflow in signed integer arithmetic is undefined. This means that it
is not possible to check for overflow after it happened, see
&lt;&lt;ex-Defensive_Coding-C-Arithmetic-bad&gt;&gt;.

:::: {#ex-Defensive_Coding-C-Arithmetic-bad .example}
::: title
Incorrect overflow detection in C
:::

``` c
```
::::

The following approaches can be used to check for overflow, without
actually causing it.

&#42; Use a wider type to perform the calculation, check that the result
is within bounds, and convert the result to the original type. All
intermediate results must be checked in this way.

&#42; Perform the calculation in the corresponding unsigned type and use
bit fiddling to detect the overflow.
&lt;&lt;ex-Defensive_Coding-C-Arithmetic-add_unsigned&gt;&gt; shows how
to perform an overflow check for unsigned integer addition. For three or
more terms, all the intermediate additions have to be checked in this
way.

:::: {#ex-Defensive_Coding-C-Arithmetic-add_unsigned .example}
::: title
Overflow checking for unsigned addition
:::

``` c
```
::::

&#42; Compute bounds for acceptable input values which are known to
avoid overflow, and reject other values. This is the preferred way for
overflow checking on multiplications, see
&lt;&lt;ex-Defensive_Coding-C-Arithmetic-mult&gt;&gt;.

:::: {#ex-Defensive_Coding-C-Arithmetic-mult .example}
::: title
Overflow checking for unsigned multiplication
:::

``` c
```
::::

Basic arithmetic operations are commutative, so for bounds checks, there
are two different but mathematically equivalent expressions. Sometimes,
one of the expressions results in better code because parts of it can be
reduced to a constant. This applies to overflow checks for
multiplication &#96;a &#42; b&#96; involving a constant &#96;a&#96;,
where the expression is reduced to &#96;b &gt; C&#96; for some constant
&#96;C&#96; determined at compile time. The other expression, &#96;b
&amp;&amp; a &gt; ((unsigned)-1) / b&#96;, is more difficult to optimize
at compile time.

When a value is converted to a signed integer, GCC always chooses the
result based on 2's complement arithmetic. This GCC extension (which is
also implemented by other compilers) helps a lot when implementing
overflow checks.

Sometimes, it is necessary to compare unsigned and signed integer
variables. This results in a compiler warning, &#42;comparison between
signed and unsigned integer expressions&#42;, because the comparison
often gives unexpected results for negative values. When adding a cast,
make sure that negative values are covered properly. If the bound is
unsigned and the checked quantity is signed, you should cast the checked
quantity to an unsigned type as least as wide as either operand type. As
a result, negative values will fail the bounds check. (You can still
check for negative values separately for clarity, and the compiler will
optimize away this redundant check.)

Legacy code should be compiled with the \[option\]&#96;-fwrapv&#96; GCC
option. As a result, GCC will provide 2's complement semantics for
integer arithmetic, including defined behavior on integer overflow.

### Global Variables {#sect-Defensive_Coding-C-Globals}

Global variables should be avoided because they usually lead to thread
safety hazards. In any case, they should be declared &#96;static&#96;,
so that access is restricted to a single translation unit.

Global constants are not a problem, but declaring them can be tricky.
&lt;&lt;ex-Defensive_Coding-C-Globals-String_Array&gt;&gt; shows how to
declare a constant array of constant strings. The second &#96;const&#96;
is needed to make the array constant, and not just the strings. It must
be placed after the &#96;&#42;&#96;, and not before it.

:::: {#ex-Defensive_Coding-C-Globals-String_Array .example}
::: title
Declaring a constant array of constant strings
:::

``` c
```
::::

Sometimes, static variables local to functions are used as a replacement
for proper memory management. Unlike non-static local variables, it is
possible to return a pointer to static local variables to the caller.
But such variables are well-hidden, but effectively global (just as
static variables at file scope). It is difficult to add thread safety
afterwards if such interfaces are used. Merely dropping the
&#96;static&#96; keyword in such cases leads to undefined behavior.

Another source for static local variables is a desire to reduce stack
space usage on embedded platforms, where the stack may span only a few
hundred bytes. If this is the only reason why the &#96;static&#96;
keyword is used, it can just be dropped, unless the object is very large
(larger than 128 kilobytes on 32-bit platforms). In the latter case, it
is recommended to allocate the object using &#96;malloc&#96;, to obtain
proper array checking, for the same reasons outlined in
&lt;&lt;sect-Defensive_Coding-C-Allocators-alloca&gt;&gt;.

## The C Standard Library {#sect-Defensive_Coding-C-Libc}

Parts of the C standard library (and the UNIX and GNU extensions) are
difficult to use, so you should avoid them.

Please check the applicable documentation before using the recommended
replacements. Many of these functions allocate buffers using
&#96;malloc&#96; which your code must deallocate explicitly using
&#96;free&#96;.

### Absolutely Banned Interfaces {#sect-Defensive_Coding-C-Absolutely-Banned}

The functions listed below must not be used because they are almost
always unsafe. Use the indicated replacements instead.

&#42; &#96;gets&#96; ⟶ &#96;fgets&#96;

&#42; &#96;getwd&#96; ⟶ &#96;getcwd&#96; or
&#96;get_current_dir_name&#96;

&#42; &#96;readdir_r&#96; ⟶ &#96;readdir&#96;

&#42; &#96;realpath&#96; (with a non-NULL second parameter) ⟶
&#96;realpath&#96; with NULL as the second parameter, or
&#96;canonicalize_file_name&#96;

The constants listed below must not be used, either. Instead, code must
allocate memory dynamically and use interfaces with length checking.

&#42; &#96;NAME_MAX&#96; (limit not actually enforced by the kernel)

&#42; &#96;PATH_MAX&#96; (limit not actually enforced by the kernel)

&#42; &#96;\_PC_NAME_MAX&#96; (This limit, returned by the
&#96;pathconf&#96; function, is not enforced by the kernel.)

&#42; &#96;\_PC_PATH_MAX&#96; (This limit, returned by the
&#96;pathconf&#96; function, is not enforced by the kernel.)

The following structure members must not be used.

&#42; &#96;f_namemax&#96; in &#96;struct statvfs&#96; (limit not
actually enforced by the kernel, see &#96;\_PC_NAME_MAX&#96; above)

### Functions to Avoid {#sect-Defensive_Coding-C-Avoid}

The following string manipulation functions can be used securely in
principle, but their use should be avoided because they are difficult to
use correctly. Calls to these functions can be replaced with
&#96;asprintf&#96; or &#96;vasprintf&#96;. (For non-GNU targets, these
functions are available from Gnulib.) In some cases, the
&#96;snprintf&#96; function might be a suitable replacement, see
&lt;&lt;sect-Defensive_Coding-C-String-Functions-Length&gt;&gt;.

&#42; &#96;sprintf&#96;

&#42; &#96;strcat&#96;

&#42; &#96;strcpy&#96;

&#42; &#96;vsprintf&#96;

Use the indicated replacements for the functions below.

&#42; &#96;alloca&#96; ⟶ &#96;malloc&#96; and &#96;free&#96; (see
&lt;&lt;sect-Defensive_Coding-C-Allocators-alloca&gt;&gt;)

&#42; &#96;putenv&#96; ⟶ explicit &#96;envp&#96; argument in process
creation (see [Specifying the Process
Environment](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-Processes-environ))

&#42; &#96;setenv&#96; ⟶ explicit &#96;envp&#96; argument in process
creation (see [Specifying the Process
Environment](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-Processes-environ))

&#42; &#96;strdupa&#96; ⟶ &#96;strdup&#96; and &#96;free&#96; (see
&lt;&lt;sect-Defensive_Coding-C-Allocators-alloca&gt;&gt;)

&#42; &#96;strndupa&#96; ⟶ &#96;strndup&#96; and &#96;free&#96; (see
&lt;&lt;sect-Defensive_Coding-C-Allocators-alloca&gt;&gt;)

&#42; &#96;system&#96; ⟶ &#96;posix_spawn&#96; or
&#96;fork&#96;/&#96;execve&#96;/ (see [Bypassing the
Shell](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-Processes-execve))

&#42; &#96;unsetenv&#96; ⟶ explicit &#96;envp&#96; argument in process
creation (see [Specifying the Process
Environment](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-Processes-environ))

### String Functions with Explicit Length Arguments {#sect-Defensive_Coding-C-String-Functions-Length}

The C run-time library provides string manipulation functions which not
just look for NUL characters for string termination, but also honor
explicit lengths provided by the caller. However, these functions
evolved over a long period of time, and the lengths mean different
things depending on the function.

#### &#96;snprintf&#96; {#sect-Defensive_Coding-C-Libc-snprintf}

The &#96;snprintf&#96; function provides a way to construct a string in
a statically-sized buffer. (If the buffer size is allocated on the heap,
consider use &#96;asprintf&#96; instead.)

``` c
```

The second argument to the &#96;snprintf&#96; call should always be the
size of the buffer in the first argument (which should be a character
array). Elaborate pointer and length arithmetic can introduce errors and
nullify the security benefits of &#96;snprintf&#96;.

In particular, &#96;snprintf&#96; is not well-suited to constructing a
string iteratively, by appending to an existing buffer.
&#96;snprintf&#96; returns one of two values, &#96;-1&#96; on errors, or
the number of characters which &#42;would have been written to the
buffer if the buffer were large enough&#42;. This means that adding the
result of &#96;snprintf&#96; to the buffer pointer to skip over the
characters just written is incorrect and risky. However, as long as the
length argument is not zero, the buffer will remain null-terminated.
&lt;&lt;ex-Defensive_Coding-C-String-Functions-snprintf-incremental&gt;&gt;
works because &#96;end -current &gt; 0&#96; is a loop invariant. After
the loop, the result string is in the &#96;buf&#96; variable.

:::: {#ex-Defensive_Coding-C-String-Functions-snprintf-incremental .example}
::: title
Repeatedly writing to a buffer using &#96;snprintf&#96;
:::

``` c
```
::::

If you want to avoid the call to &#96;strlen&#96; for performance
reasons, you have to check for a negative return value from
&#96;snprintf&#96; and also check if the return value is equal to the
specified buffer length or larger. Only if neither condition applies,
you may advance the pointer to the start of the write buffer by the
number return by &#96;snprintf&#96;. However, this optimization is
rarely worthwhile.

Note that it is not permitted to use the same buffer both as the
destination and as a source argument.

#### &#96;vsnprintf&#96; and Format Strings {#sect-Defensive_Coding-C-Libc-vsnprintf}

If you use &#96;vsnprintf&#96; (or &#96;vasprintf&#96; or even
&#96;snprintf&#96;) with a format string which is not a constant, but a
function argument, it is important to annotate the function with a
&#96;format&#96; function attribute, so that GCC can warn about misuse
of your function (see
&lt;&lt;ex-Defensive_Coding-C-String-Functions-format-Attribute&gt;&gt;).

:::: {#ex-Defensive_Coding-C-String-Functions-format-Attribute .example}
::: title
The &#96;format&#96; function attribute
:::

``` c
```
::::

#### &#96;strncpy&#96; {#sect-Defensive_Coding-C-Libc-strncpy}

The &#96;strncpy&#96; function does not ensure that the target buffer is
null-terminated. A common idiom for ensuring NUL termination is:

``` c
```

Another approach uses the &#96;strncat&#96; function for this purpose:

``` c
```

#### &#96;strncat&#96; {#sect-Defensive_Coding-C-Libc-strncat}

The length argument of the &#96;strncat&#96; function specifies the
maximum number of characters copied from the source buffer, excluding
the terminating NUL character. This means that the required number of
bytes in the destination buffer is the length of the original string,
plus the length argument in the &#96;strncat&#96; call, plus one.
Consequently, this function is rarely appropriate for performing a
length-checked string operation, with the notable exception of the
&#96;strcpy&#96; emulation described in
&lt;&lt;sect-Defensive_Coding-C-Libc-strncpy&gt;&gt;.

To implement a length-checked string append, you can use an approach
similar to
&lt;&lt;ex-Defensive_Coding-C-String-Functions-snprintf-incremental&gt;&gt;:

``` c
```

In many cases, including this one, the string concatenation can be
avoided by combining everything into a single format string:

``` c
```

But you should must not dynamically construct format strings to avoid
concatenation because this would prevent GCC from type-checking the
argument lists.

It is not possible to use format strings like &#96;\'%s%s\'&#96; to
implement concatenation, unless you use separate buffers.
&#96;snprintf&#96; does not support overlapping source and target
strings.

#### &#96;strlcpy&#96; and &#96;strlcat&#96; {#_96strlcpy96_and_96strlcat96}

Some systems support &#96;strlcpy&#96; and &#96;strlcat&#96; functions
which behave this way, but these functions are not part of GNU libc.
&#96;strlcpy&#96; is often replaced with &#96;snprintf&#96; with a
&#96;\'%s\'&#96; format string. See
&lt;&lt;sect-Defensive_Coding-C-Libc-strncpy&gt;&gt; for a caveat
related to the &#96;snprintf&#96; return value.

To emulate &#96;strlcat&#96;, use the approach described in
&lt;&lt;sect-Defensive_Coding-C-Libc-strncat&gt;&gt;.

#### ISO C11 Annex K &#42;&#96;\_s&#96; functions {#_iso_c11_annex_k_4296_s96_functions}

ISO C11 adds another set of length-checking functions, but GNU libc
currently does not implement them.

#### Other &#96;strn&#42;&#96; and &#96;stpn&#42;&#96; functions {#_other_96strn4296_and_96stpn4296_functions}

GNU libc contains additional functions with different variants of length
checking. Consult the documentation before using them to find out what
the length actually means.

### Using tricky syscalls or library functions {#_using_tricky_syscalls_or_library_functions}

#### &#96;readlink&#96; {#_96readlink96}

This is the hardest system call to use correctly because of everything
you have to do

&#42; The buf should be of PATH_MAX length, that includes space for the
terminating NUL character. &#42; The bufsize should be
&#96;sizeof(buf) - 1&#96; &#42; &#96;readlink&#96; return value should
be caught as a signed integer (ideally type &#96;ssize_t&#96;). &#42; It
should be checked for &lt; 0 for indication of errors. &#42; The caller
needs to \'\\0\' -terminate the buffer using the returned value as an
index.

#### &#96;chroot&#96; {#_96chroot96}

&#42; Target dir should be writable only by root (this implies owned
by). &#42; Must call &#96;chdir&#96; immediately after chroot or you are
not really in the changed root.

#### &#96;stat&#96;, &#96;lstat&#96;, &#96;fstatat&#96; {#_96stat96_96lstat96_96fstatat96}

&#42; These functions have an inherent race in that you operate on the
path name which could change in the mean time. Using fstat is
recommended when stat is used. &#42; If &#96;S_ISLNK&#96; macro is used,
the stat buffer MUST come from lstat or from fstatat with
&#96;AT_SYMLINK_NOFOLLOW&#96; &#42; If you are doing something really
important, call fstat after opening and compare the before and after
stat buffers before trusting them.

#### &#96;setgid&#96;, &#96;setuid&#96;: {#_96setgid96_96setuid96}

&#42; Call these in the right order: groups and then uid. &#42; Always
check the return code. &#42; If &#96;setgid&#96; &amp; &#96;setuid&#96;
are used, supplemental groups are not reset. This must be done with
setgroups or initgroups before the uid change.

## Memory Allocators {#sect-Defensive_Coding-C-Allocators}

### &#96;malloc&#96; and Related Functions {#_96malloc96_and_related_functions}

The C library interfaces for memory allocation are provided by
&#96;malloc&#96;, &#96;free&#96; and &#96;realloc&#96;, and the
&#96;calloc&#96; function. In addition to these generic functions, there
are derived functions such as &#96;strdup&#96; which perform allocation
using &#96;malloc&#96; internally, but do not return untyped heap memory
(which could be used for any object).

The C compiler knows about these functions and can use their expected
behavior for optimizations. For instance, the compiler assumes that an
existing pointer (or a pointer derived from an existing pointer by
arithmetic) will not point into the memory area returned by
&#96;malloc&#96;.

If the allocation fails, &#96;realloc&#96; does not free the old
pointer. Therefore, the idiom &#96;ptr = realloc(ptr, size);&#96; is
wrong because the memory pointed to by &#96;ptr&#96; leaks in case of an
error.

#### Memory leaks {#_memory_leaks}

After a memory area has been allocated with functions like
&#96;malloc&#96;, &#96;calloc&#96;, etc. and it is no longer necessary,
it must be freed in order for the system to release the memory region
and re-use it if necessary. Failing to do so may lead to the application
using more memory than necessary and, in some cases, crashing due to no
more memory being available.

If portability is not important in your program, an alternative way of
automatic memory management is to leverage the &#96;cleanup&#96;
attribute supported by the recent versions of GCC and Clang. If a local
variable is declared with the attribute, the specified cleanup function
will be called when the variable goes out of scope.

``` c
static inline void freep(void \&#42;p) {
free(\&#42;(void\&#42;\&#42;) p);
}

void somefunction(const char \&#42;param) {
if (strcmp(param, 'do_something_complex') == 0) {
__attribute__((cleanup(freep))) char \&#42;ptr = NULL;

/\&#42; Allocate a temporary buffer \&#42;/
ptr = malloc(size);

/\&#42; Do something on it, but do not need to manually call free() \&#42;/
}
}
```

#### Use-after-free errors {#sect-Defensive_Coding-C-Use-After-Free}

After &#96;free&#96;, the pointer is invalid. Further pointer
dereferences are not allowed (and are usually detected by
\[application\]&#42;valgrind&#42;). Less obvious is that any
&#42;use&#42; of the old pointer value is not allowed, either. In
particular, comparisons with any other pointer (or the null pointer) are
undefined according to the C standard.

The same rules apply to &#96;realloc&#96; if the memory area cannot be
enlarged in-place. For instance, the compiler may assume that a
comparison between the old and new pointer will always return false, so
it is impossible to detect movement this way.

On a related note, &#96;realloc&#96; frees the memory area if the new
size is zero. If the size unintentionally becomes zero, as a result of
unsigned integer wrap-around for instance, the following idiom causes a
double-free.

``` c
new_size = size + x; /\&#42; 'x' is a very large value and the result wraps around to zero \&#42;/
new_ptr = realloc(ptr, new_size);
if (!new_ptr) {
free(ptr);
}
```

#### Handling Memory Allocation Errors {#_handling_memory_allocation_errors}

Recovering from out-of-memory errors is often difficult or even
impossible. In these cases, &#96;malloc&#96; and other allocation
functions return a null pointer. Dereferencing this pointer lead to a
crash. Such dereferences can even be exploitable for code execution if
the dereference is combined with an array subscript.

In general, if you cannot check all allocation calls and handle failure,
you should abort the program on allocation failure, and not rely on the
null pointer dereference to terminate the process. See [Recommendations
for Manually-written
Decoders](tasks/Tasks-Serialization.adoc&#35;sect-Defensive_Coding-Tasks-Serialization-Decoders)
for related memory allocation concerns.

### &#96;alloca&#96; and Other Forms of Stack-based Allocation {#sect-Defensive_Coding-C-Allocators-alloca}

Allocation on the stack is risky because stack overflow checking is
implicit. There is a guard page at the end of the memory area reserved
for the stack. If the program attempts to read from or write to this
guard page, a &#96;SIGSEGV&#96; signal is generated and the program
typically terminates.

This is sufficient for detecting typical stack overflow situations such
as unbounded recursion, but it fails when the stack grows in increments
larger than the size of the guard page. In this case, it is possible
that the stack pointer ends up pointing into a memory area which has
been allocated for a different purposes. Such misbehavior can be
exploitable.

A common source for large stack growth are calls to &#96;alloca&#96; and
related functions such as &#96;strdupa&#96;. These functions should be
avoided because of the lack of error checking. (They can be used safely
if the allocated size is less than the page size (typically, 4096
bytes), but this case is relatively rare.) Additionally, relying on
&#96;alloca&#96; makes it more difficult to reorganize the code because
it is not allowed to use the pointer after the function calling
&#96;alloca&#96; has returned, even if this function has been inlined
into its caller.

Similar concerns apply to &#42;variable-length arrays&#42; (VLAs), a
feature of the C99 standard which started as a GNU extension. For large
objects exceeding the page size, there is no error checking, either.

In both cases, negative or very large sizes can trigger a stack-pointer
wraparound, and the stack pointer ends up pointing into caller stack
frames, which is fatal and can be exploitable.

If you want to use &#96;alloca&#96; or VLAs for performance reasons,
consider using a small on-stack array (less than the page size, large
enough to fulfill most requests). If the requested size is small enough,
use the on-stack array. Otherwise, call &#96;malloc&#96;. When exiting
the function, check if &#96;malloc&#96; had been called, and free the
buffer as needed.

Remember that memory allocated on the stack through &#96;alloca&#96; is
released at the end of the function and not at the end of the block
where it is defined, thus it is reccommended to not call
&#96;alloca&#96; inside a loop. In this regard, VLA behaves better,
considering the memory allocated with VLA is released at the end of the
block that defines them. Do not mix VLA and &#96;alloca&#96; though,
otherwise this behaviour is not guaranteed for VLA either!

### Array Allocation {#sect-Defensive_Coding-C-Allocators-Arrays}

When allocating arrays, it is important to check for overflows. The
&#96;calloc&#96; function performs such checks.

If &#96;malloc&#96; or &#96;realloc&#96; is used, the size check must be
written manually. For instance, to allocate an array of &#96;n&#96;
elements of type &#96;T&#96;, check that the requested size is not
greater than &#96;((size_t) -1) / sizeof(T)&#96;. See
&lt;&lt;sect-Defensive_Coding-C-Arithmetic&gt;&gt;.

GNU libc provides a dedicated function &#96;reallocarray&#96; that
allocates an array with those checks performed internally. However, care
must be taken if portability is important: while the interface
originated in OpenBSD and has been adopted in many other platforms,
NetBSD exposes an incompatible behavior with the same interface.

### Custom Memory Allocators {#sect-Defensive_Coding-C-Allocators-Custom}

Custom memory allocates come in two forms: replacements for
&#96;malloc&#96;, and completely different interfaces for memory
management. Both approaches can reduce the effectiveness of
\[application\]&#42;valgrind&#42; and similar tools, and the heap
corruption detection provided by GNU libc, so they should be avoided.

Memory allocators are difficult to write and contain many performance
and security pitfalls.

&#42; When computing array sizes or rounding up allocation requests (to
the next allocation granularity, or for alignment purposes), checks for
arithmetic overflow are required.

&#42; Size computations for array allocations need overflow checking.
See &lt;&lt;sect-Defensive_Coding-C-Allocators-Arrays&gt;&gt;.

&#42; It can be difficult to beat well-tuned general-purpose allocators.
In micro benchmarks, pool allocators can show huge wins, and
size-specific pools can reduce internal fragmentation. But often,
utilization of individual pools is poor, and external fragmentation
increases the overall memory usage.

### Conservative Garbage Collection {#_conservative_garbage_collection}

Garbage collection can be an alternative to explicit memory management
using &#96;malloc&#96; and &#96;free&#96;. The Boehm-Dehmers-Weiser
allocator can be used from C programs, with minimal type annotations.
Performance is competitive with &#96;malloc&#96; on 64-bit
architectures, especially for multi-threaded programs. The
stop-the-world pauses may be problematic for some real-time
applications, though.

However, using a conservative garbage collector may reduce opportunities
for code reduce because once one library in a program uses garbage
collection, the whole process memory needs to be subject to it, so that
no pointers are missed. The Boehm-Dehmers-Weiser collector also reserves
certain signals for internal use, so it is not fully transparent to the
rest of the program.

## Other C-related Topics {#sect-Defensive_Coding-C-Other}

### Wrapper Functions {#sect-Defensive_Coding-C-Wrapper-Functions}

Some libraries provide wrappers for standard library functions. Common
cases include allocation functions such as &#96;xmalloc&#96; which abort
the process on allocation failure (instead of returning a &#96;NULL&#96;
pointer), or alternatives to relatively recent library additions such as
&#96;snprintf&#96; (along with implementations for systems which lack
them).

In general, such wrappers are a bad idea, particularly if they are not
implemented as inline functions or preprocessor macros. The compiler
lacks knowledge of such wrappers outside the translation unit which
defines them, which means that some optimizations and security checks
are not performed. Adding &#96;+*attribute*+&#96; annotations to
function declarations can remedy this to some extent, but these
annotations have to be maintained carefully for feature parity with the
standard implementation.

At the minimum, you should apply these attributes:

&#42; If you wrap function which accepts are GCC-recognized format
string (for example, a &#96;printf&#96;-style function used for
logging), you should add a suitable &#96;format&#96; attribute, as in
&lt;&lt;ex-Defensive_Coding-C-String-Functions-format-Attribute&gt;&gt;.

&#42; If you wrap a function which carries a
&#96;warn_unused_result&#96; attribute and you propagate its return
value, your wrapper should be declared with &#96;warn_unused_result&#96;
as well.

&#42; Duplicating the buffer length checks based on the
&#96;+\_\_builtin_object_size+&#96; GCC builtin is desirable if the
wrapper processes arrays. (This functionality is used by the
&#96;-D_FORTIFY_SOURCE=2&#96; checks to guard against static buffer
overflows.) However, designing appropriate interfaces and implementing
the checks may not be entirely straightforward.

For other attributes (such as &#96;malloc&#96;), careful analysis and
comparison with the compiler documentation is required to check if
propagating the attribute is appropriate. Incorrectly applied attributes
can result in undesired behavioral changes in the compiled code.

### Common mistakes {#sect-Defensive_Coding-C-Common-Mistakes}

#### Mistakes in macros {#_mistakes_in_macros}

A macro is a name given to a block of C statements as a pre-processor
directive. Being a pre-processor the block of code is transformed by the
compiler before being compiled.

A macro starts with the preprocessor directive, &#35;define. It can
define a single value or any \'substitution\', syntactically valid or
not.

A common mistake when working with macros is that programmers treat
arguments to macros like they would functions. This becomes an issue
when the argument may be expanded multiple times in a macro.

For example:

macro-misuse.c

``` C
\&#35;define simple(thing) do { \
if (thing \&lt; 1) { \
y = thing; \
} \
else if (thing \&gt; 100) { \
y = thing \&#42; 2 + thing; \
} \
else  { \
y = 200; \
} \
} while (0)

int main(void) {
int x = 200;
int y = 0;
simple(x++);

return 0;
}
```

Each pass through the simple() macro would mean that x could be expanded
in-place each time \'thing\' was mentioned.

The \'main\' function would be processed and expanded as follows:

macro-misuse-post-processing.c

``` C
int main(void) {
int x = 200;
int y = 0;
do {
if ( x++ \&lt; 1) {
y = x++;
}
else if (thing \&gt; 100) {
y = x++ \&#42; 2 + x++;
}
else  {
x = 200;
}
} while (0)

return 0;
}
```

Each evaluation of the argument to \'simple\' (x++) would be executed
each time it was referenced.

While this may be \'expected\' behaviour by the original creator, large
projects may have programmers who were unaware of how the macro may
expand and this may introduce unexpected behaviour, especially if the
value is later used as indexing into an array or able to be overflowed.

# The C++ Programming Language {#_the_c_programming_language_2}

## The Core Language {#sect-Defensive_Coding-CXX-Language}

C++ includes a large subset of the C language. As far as the C subset is
used, the recommendations in [Defensive Coding in
C](programming-languages/C.adoc&#35;chap-Defensive_Coding-C) apply.

### Array Allocation with &#96;operator new\[\]&#96; {#_array_allocation_with_96operator_new96}

For very large values of &#96;n&#96;, an expression like &#96;new
T\[n\]&#96; can return a pointer to a heap region which is too small. In
other words, not all array elements are actually backed with heap memory
reserved to the array. Current GCC versions generate code that performs
a computation of the form &#96;sizeof(T) &#42; size_t(n) +
cookie_size&#96;, where &#96;cookie_size&#96; is currently at most 8.
This computation can overflow, and GCC versions prior to 4.8 generated
code which did not detect this. (Fedora 18 was the first release which
fixed this in GCC.)

The &#96;std::vector&#96; template can be used instead an explicit array
allocation. (The GCC implementation detects overflow internally.)

If there is no alternative to &#96;operator new\[\]&#96; and the sources
will be compiled with older GCC versions, code which allocates arrays
with a variable length must check for overflow manually. For the
&#96;new T\[n\]&#96; example, the size check could be &#96;n \|\| (n
&gt; 0 &amp;&amp; n &gt; (size_t(-1) - 8) / sizeof(T))&#96;. (See
[Recommendations for Integer
Arithmetic](programming-languages/C.adoc&#35;sect-Defensive_Coding-C-Arithmetic))
If there are additional dimensions (which must be constants according to
the C++ standard), these should be included as factors in the divisor.

These countermeasures prevent out-of-bounds writes and potential code
execution. Very large memory allocations can still lead to a denial of
service. [Recommendations for Manually-written
Decoders](tasks/Tasks-Serialization.adoc&#35;sect-Defensive_Coding-Tasks-Serialization-Decoders)
contains suggestions for mitigating this problem when processing
untrusted data.

See [Array
Allocation](tasks/programming-languages/C.adoc&#35;sect-Defensive_Coding-C-Allocators-Arrays)
for array allocation advice for C-style memory allocation.

### Overloading {#_overloading}

Do not overload functions with versions that have different security
characteristics. For instance, do not implement a function
&#96;strcat&#96; which works on &#96;std::string&#96; arguments.
Similarly, do not name methods after such functions.

### ABI compatibility and preparing for security updates {#_abi_compatibility_and_preparing_for_security_updates}

A stable binary interface (ABI) is vastly preferred for security
updates. Without a stable ABI, all reverse dependencies need
recompiling, which can be a lot of work and could even be impossible in
some cases. Ideally, a security update only updates a single dynamic
shared object, and is picked up automatically after restarting affected
processes.

Outside of extremely performance-critical code, you should ensure that a
wide range of changes is possible without breaking ABI. Some very basic
guidelines are:

&#42; Avoid inline functions.

&#42; Use the pointer-to-implementation idiom.

&#42; Try to avoid templates. Use them if the increased type safety
provides a benefit to the programmer.

&#42; Move security-critical code out of templated code, so that it can
be patched in a central place if necessary.

The KDE project publishes a document with more extensive guidelines on
ABI-preserving changes to C++ code, [Policies/Binary Compatibility
Issues With
C++](https://community.kde.org/Policies/Binary_Compatibility_Issues_With_C%2B%2B)
(&#42;d-pointer&#42; refers to the pointer-to-implementation idiom).

### C++0X and C++11 Support {#sect-Defensive_Coding-CXX-Language-CXX11}

GCC offers different language compatibility modes:

&#42; \[option\]&#96;-std=c++98&#96; for the original 1998 C++ standard

&#42; \[option\]&#96;-std=c++03&#96; for the 1998 standard with the
changes from the TR1 technical report

&#42; \[option\]&#96;-std=c++11&#96; for the 2011 C++ standard. This
option should not be used.

&#42; \[option\]&#96;-std=c++0x&#96; for several different versions of
C++11 support in development, depending on the GCC version. This option
should not be used.

For each of these flags, there are variants which also enable GNU
extensions (mostly language features also found in C99 or C11):

&#42; \[option\]&#96;-std=gnu98\\&#96; \\&#42;
\[option\]\\&#96;-std=gnu03&#96; &#42; \[option\]&#96;-std=gnu++11&#96;

Again, \[option\]&#96;-std=gnu++11&#96; should not be used.

If you enable C++11 support, the ABI of the standard C++ library
&#96;libstdc++&#96; will change in subtle ways. Currently, no C++
libraries are compiled in C++11 mode, so if you compile your code in
C++11 mode, it will be incompatible with the rest of the system.
Unfortunately, this is also the case if you do not use any C++11
features. Currently, there is no safe way to enable C++11 mode (except
for freestanding applications).

The meaning of C++0X mode changed from GCC release to GCC release.
Earlier versions were still ABI-compatible with C++98 mode, but in the
most recent versions, switching to C++0X mode activates C++11 support,
with its compatibility problems.

Some C++11 features (or approximations thereof) are available with TR1
support, that is, with \[option\]&#96;-std=c03\\&#96; or
\[option\]\\&#96;-std=gnu03&#96; and in the &#96;&lt;tr1/&#42;&gt;&#96;
header files. This includes &#96;std::tr1::shared_ptr&#96; (from
&#96;&lt;tr1/memory&gt;&#96;) and &#96;std::tr1::function&#96; (from
&#96;&lt;tr1/functional&gt;&#96;). For other C++11 features, the Boost
C++ library contains replacements.

## The C++ Standard Library {#sect-Defensive_Coding-CXX-Std}

The C++ standard library includes most of its C counterpart by
reference, see [Defensive Coding in
C](programming-languages/C.adoc&#35;chap-Defensive_Coding-C).

### Functions That Are Difficult to Use {#sect-Defensive_Coding-CXX-Std-Functions}

This section collects functions and function templates which are part of
the standard library and are difficult to use.

#### Unpaired Iterators {#sect-Defensive_Coding-CXX-Std-Functions-Unpaired_Iterators}

Functions which use output operators or iterators which do not come in
pairs (denoting ranges) cannot perform iterator range checking. (See
&lt;&lt;sect-Defensive_Coding-CXX-Std-Iterators&gt;&gt;) Function
templates which involve output iterators are particularly dangerous:

&#42; &#96;std::copy&#96;

&#42; &#96;std::copy_backward&#96;

&#42; &#96;std::copy_if&#96;

&#42; &#96;std::move&#96; (three-argument variant)

&#42; &#96;std::move_backward&#96;

&#42; &#96;std::partition_copy_if&#96;

&#42; &#96;std::remove_copy&#96;

&#42; &#96;std::remove_copy_if&#96;

&#42; &#96;std::replace_copy&#96;

&#42; &#96;std::replace_copy_if&#96;

&#42; &#96;std::swap_ranges&#96;

&#42; &#96;std::transform&#96;

In addition, &#96;std::copy_n&#96;, &#96;std::fill_n&#96; and
&#96;std::generate_n&#96; do not perform iterator checking, either, but
there is an explicit count which has to be supplied by the caller, as
opposed to an implicit length indicator in the form of a pair of forward
iterators.

These output-iterator-expecting functions should only be used with
unlimited-range output iterators, such as iterators obtained with the
&#96;std::back_inserter&#96; function.

Other functions use single input or forward iterators, which can read
beyond the end of the input range if the caller is not careful:

&#42; &#96;std::equal&#96;

&#42; &#96;std::is_permutation&#96;

&#42; &#96;std::mismatch&#96;

### String Handling with &#96;std::string&#96; {#sect-Defensive_Coding-CXX-Std-String}

The &#96;std::string&#96; class provides a convenient way to handle
strings. Unlike C strings, &#96;std::string&#96; objects have an
explicit length (and can contain embedded NUL characters), and storage
for its characters is managed automatically. This section discusses
&#96;std::string&#96;, but these observations also apply to other
instances of the &#96;std::basic_string&#96; template.

The pointer returned by the &#96;data()&#96; member function does not
necessarily point to a NUL-terminated string. To obtain a C-compatible
string pointer, use &#96;c_str()&#96; instead, which adds the NUL
terminator.

The pointers returned by the &#96;data()&#96; and &#96;c_str()&#96;
functions and iterators are only valid until certain events happen. It
is required that the exact &#96;std::string&#96; object still exists
(even if it was initially created as a copy of another string object).
Pointers and iterators are also invalidated when non-const member
functions are called, or functions with a non-const reference parameter.
The behavior of the GCC implementation deviates from that required by
the C++ standard if multiple threads are present. In general, only the
first call to a non-const member function after a structural
modification of the string (such as appending a character) is
invalidating, but this also applies to member function such as the
non-const version of &#96;begin()&#96;, in violation of the C++
standard.

Particular care is necessary when invoking the &#96;c_str()&#96; member
function on a temporary object. This is convenient for calling C
functions, but the pointer will turn invalid as soon as the temporary
object is destroyed, which generally happens when the outermost
expression enclosing the expression on which &#96;c_str()&#96; is called
completes evaluation. Passing the result of &#96;c_str()&#96; to a
function which does not store or otherwise leak that pointer is safe,
though.

Like with &#96;std::vector&#96; and &#96;std::array&#96;, subscribing
with &#96;operator\[\]&#96; does not perform bounds checks. Use the
&#96;at(size_type)&#96; member function instead. See
&lt;&lt;sect-Defensive_Coding-CXX-Std-Subscript&gt;&gt;. Furthermore,
accessing the terminating NUL character using &#96;operator\[\]&#96; is
not possible. (In some implementations, the &#96;c_str()&#96; member
function writes the NUL character on demand.)

Never write to the pointers returned by &#96;data()&#96; or
&#96;c_str()&#96; after casting away &#96;const&#96;. If you need a
C-style writable string, use a &#96;std::vector&lt;char&gt;&#96; object
and its &#96;data()&#96; member function. In this case, you have to
explicitly add the terminating NUL character.

GCC's implementation of &#96;std::string&#96; is currently based on
reference counting. It is expected that a future version will remove the
reference counting, due to performance and conformance issues. As a
result, code that implicitly assumes sharing by holding to pointers or
iterators for too long will break, resulting in run-time crashes or
worse. On the other hand, non-const iterator-returning functions will no
longer give other threads an opportunity for invalidating existing
iterators and pointers because iterator invalidation does not depend on
sharing of the internal character array object anymore.

### Containers and &#96;operator\[\]&#96; {#sect-Defensive_Coding-CXX-Std-Subscript}

Many sequence containers similar to &#96;std::vector&#96; provide both
&#96;operator\[\](size_type)&#96; and a member function
&#96;at(size_type)&#96;. This applies to &#96;std::vector&#96; itself,
&#96;std::array&#96;, &#96;std::string&#96; and other instances of
&#96;std::basic_string&#96;.

&#96;operator\[\](size_type)&#96; is not required by the standard to
perform bounds checking (and the implementation in GCC does not). In
contrast, &#96;at(size_type)&#96; must perform such a check. Therefore,
in code which is not performance-critical, you should prefer
&#96;at(size_type)&#96; over &#96;operator\[\](size_type)&#96;, even
though it is slightly more verbose.

The &#96;front()&#96; and &#96;back()&#96; member functions are
undefined if a vector object is empty. You can use &#96;vec.at(0)&#96;
and &#96;vec.at(vec.size() - 1)&#96; as checked replacements. For an
empty vector, &#96;data()&#96; is defined; it returns an arbitrary
pointer, but not necessarily the NULL pointer.

### Iterators {#sect-Defensive_Coding-CXX-Std-Iterators}

Iterators do not perform any bounds checking. Therefore, all functions
that work on iterators should accept them in pairs, denoting a range,
and make sure that iterators are not moved outside that range. For
forward iterators and bidirectional iterators, you need to check for
equality before moving the first or last iterator in the range. For
random-access iterators, you need to compute the difference before
adding or subtracting an offset. It is not possible to perform the
operation and check for an invalid operator afterwards.

Output iterators cannot be compared for equality. Therefore, it is
impossible to write code that detects that it has been supplied an
output area that is too small, and their use should be avoided.

These issues make some of the standard library functions difficult to
use correctly, see
&lt;&lt;sect-Defensive_Coding-CXX-Std-Functions-Unpaired_Iterators&gt;&gt;.

# The Java Programming Language {#_the_java_programming_language}

## The Core Language {#sect-Defensive_Coding-Java-Language}

Implementations of the Java programming language provide strong memory
safety, even in the presence of data races in concurrent code. This
prevents a large range of security vulnerabilities from occurring,
unless certain low-level features are used; see
&lt;&lt;sect-Defensive_Coding-Java-LowLevel&gt;&gt;.

### Increasing Robustness when Reading Arrays {#sect-Defensive_Coding-Java-Language-ReadArray}

External data formats often include arrays, and the data is stored as an
integer indicating the number of array elements, followed by this number
of elements in the file or protocol data unit. This length specified can
be much larger than what is actually available in the data source.

To avoid allocating extremely large amounts of data, you can allocate a
small array initially and grow it as you read more data, implementing an
exponential growth policy. See the &#96;readBytes(InputStream, int)&#96;
function in &lt;&lt;ex-Defensive_Coding-Java-Language-ReadArray&gt;&gt;.

:::: {#ex-Defensive_Coding-Java-Language-ReadArray .example}
::: title
Incrementally reading a byte array
:::

``` java
```
::::

When reading data into arrays, hash maps or hash sets, use the default
constructor and do not specify a size hint. You can simply add the
elements to the collection as you read them.

### Resource Management {#sect-Defensive_Coding-Java-Language-Resources}

Unlike C++, Java does not offer destructors which can deallocate
resources in a predictable fashion. All resource management has to be
manual, at the usage site. (Finalizers are generally not usable for
resource management, especially in high-performance code; see
&lt;&lt;sect-Defensive_Coding-Java-Language-Finalizers&gt;&gt;.)

The first option is the &#96;try&#96;-&#96;finally&#96; construct, as
shown in &lt;&lt;ex-Defensive_Coding-Java-Language-Finally&gt;&gt;. The
code in the &#96;finally&#96; block should be as short as possible and
should not throw any exceptions.

:::: {#ex-Defensive_Coding-Java-Language-Finally .example}
::: title
Resource management with a &#96;try&#96;-&#96;finally&#96; block
:::

``` java
```
::::

Note that the resource allocation happens &#42;outside&#42; the
&#96;try&#96; block, and that there is no &#96;null&#96; check in the
&#96;finally&#96; block. (Both are common artifacts stemming from IDE
code templates.)

If the resource object is created freshly and implements the
&#96;java.lang.AutoCloseable&#96; interface, the code in
&lt;&lt;ex-Defensive_Coding-Java-Language-TryWithResource&gt;&gt; can be
used instead. The Java compiler will automatically insert the
&#96;close()&#96; method call in a synthetic &#96;finally&#96; block.

:::: {#ex-Defensive_Coding-Java-Language-TryWithResource .example}
::: title
Resource management using the &#96;try&#96;-with-resource construct
:::

``` java
```
::::

To be compatible with the &#96;try&#96;-with-resource construct, new
classes should name the resource deallocation method &#96;close()&#96;,
and implement the &#96;AutoCloseable&#96; interface (the latter breaking
backwards compatibility with Java 6). However, using the
&#96;try&#96;-with-resource construct with objects that are not freshly
allocated is at best awkward, and an explicit &#96;finally&#96; block is
usually the better approach.

In general, it is best to design the programming interface in such a way
that resource deallocation methods like &#96;close()&#96; cannot throw
any (checked or unchecked) exceptions, but this should not be a reason
to ignore any actual error conditions.

### Finalizers {#sect-Defensive_Coding-Java-Language-Finalizers}

Finalizers can be used a last-resort approach to free resources which
would otherwise leak. Finalization is unpredictable, costly, and there
can be a considerable delay between the last reference to an object
going away and the execution of the finalizer. Generally, manual
resource management is required; see
&lt;&lt;sect-Defensive_Coding-Java-Language-Resources&gt;&gt;.

Finalizers should be very short and should only deallocate native or
other external resources held directly by the object being finalized. In
general, they must use synchronization: Finalization necessarily happens
on a separate thread because it is inherently concurrent. There can be
multiple finalization threads, and despite each object being finalized
at most once, the finalizer must not assume that it has exclusive access
to the object being finalized (in the &#96;this&#96; pointer).

Finalizers should not deallocate resources held by other objects,
especially if those objects have finalizers on their own. In particular,
it is a very bad idea to define a finalizer just to invoke the resource
deallocation method of another object, or overwrite some pointer fields.

Finalizers are not guaranteed to run at all. For instance, the virtual
machine (or the machine underneath) might crash, preventing their
execution.

Objects with finalizers are garbage-collected much later than objects
without them, so using finalizers to zero out key material (to reduce
its undecrypted lifetime in memory) may have the opposite effect,
keeping objects around for much longer and prevent them from being
overwritten in the normal course of program execution.

For the same reason, code which allocates objects with finalizers at a
high rate will eventually fail (likely with a
&#96;java.lang.OutOfMemoryError&#96; exception) because the virtual
machine has finite resources for keeping track of objects pending
finalization. To deal with that, it may be necessary to recycle objects
with finalizers.

The remarks in this section apply to finalizers which are implemented by
overriding the &#96;finalize()&#96; method, and to custom finalization
using reference queues.

### Recovering from Exceptions and Errors {#sect-Defensive_Coding-Java-Language-Exceptions}

Java exceptions come in three kinds, all ultimately deriving from
&#96;java.lang.Throwable&#96;:

&#42; &#42;Run-time exceptions&#42; do not have to be declared
explicitly and can be explicitly thrown from any code, by calling code
which throws them, or by triggering an error condition at run time, like
division by zero, or an attempt at an out-of-bounds array access. These
exceptions derive from from the &#96;java.lang.RuntimeException&#96;
class (perhaps indirectly).

&#42; &#42;Checked exceptions&#42; have to be declared explicitly by
functions that throw or propagate them. They are similar to run-time
exceptions in other regards, except that there is no language construct
to throw them (except the &#96;throw&#96; statement itself). Checked
exceptions are only present at the Java language level and are only
enforced at compile time. At run time, the virtual machine does not know
about them and permits throwing exceptions from any code. Checked
exceptions must derive (perhaps indirectly) from the
&#96;java.lang.Exception&#96; class, but not from
&#96;java.lang.RuntimeException&#96;.

&#42; &#42;Errors&#42; are exceptions which typically reflect serious
error conditions. They can be thrown at any point in the program, and do
not have to be declared (unlike checked exceptions). In general, it is
not possible to recover from such errors; more on that below, in
&lt;&lt;sect-Defensive_Coding-Java-Language-Exceptions-Errors&gt;&gt;.
Error classes derive (perhaps indirectly) from
&#96;java.lang.Error&#96;, or from &#96;java.lang.Throwable&#96;, but
not from &#96;java.lang.Exception&#96;.

The general expectation is that run-time errors are avoided by careful
programming (e.g., not dividing by zero). Checked exception are expected
to be caught as they happen (e.g., when an input file is unexpectedly
missing). Errors are impossible to predict and can happen at any point
and reflect that something went wrong beyond all expectations.

#### The Difficulty of Catching Errors {#sect-Defensive_Coding-Java-Language-Exceptions-Errors}

Errors (that is, exceptions which do not (indirectly) derive from
&#96;java.lang.Exception&#96;), have the peculiar property that catching
them is problematic. There are several reasons for this:

&#42; The error reflects a failed consistenty check, for example,
&#96;java.lang.AssertionError&#96;.

&#42; The error can happen at any point, resulting in inconsistencies
due to half-updated objects. Examples are
&#96;java.lang.ThreadDeath&#96;, &#96;java.lang.OutOfMemoryError&#96;
and &#96;java.lang.StackOverflowError&#96;.

&#42; The error indicates that virtual machine failed to provide some
semantic guarantees by the Java programming language.
&#96;java.lang.ExceptionInInitializerError&#96; is an example---it can
leave behind a half-initialized class.

In general, if an error is thrown, the virtual machine should be
restarted as soon as possible because it is in an inconsistent state.
Continuing running as before can have unexpected consequences. However,
there are legitimate reasons for catching errors because not doing so
leads to even greater problems.

Code should be written in a way that avoids triggering errors. See
&lt;&lt;sect-Defensive_Coding-Java-Language-ReadArray&gt;&gt; for an
example.

It is usually necessary to log errors. Otherwise, no trace of the
problem might be left anywhere, making it very difficult to diagnose
related failures. Consequently, if you catch
&#96;java.lang.Exception&#96; to log and suppress all unexpected
exceptions (for example, in a request dispatching loop), you should
consider switching to &#96;java.lang.Throwable&#96; instead, to also
cover errors.

The other reason mainly applies to such request dispatching loops: If
you do not catch errors, the loop stops looping, resulting in a denial
of service.

However, if possible, catching errors should be coupled with a way to
signal the requirement of a virtual machine restart.

## Low-level Features of the Virtual Machine {#sect-Defensive_Coding-Java-LowLevel}

### Reflection and Private Parts {#sect-Defensive_Coding-Java-Reflection}

The &#96;setAccessible(boolean)&#96; method of the
&#96;java.lang.reflect.AccessibleObject&#96; class allows a program to
disable language-defined access rules for specific constructors,
methods, or fields. Once the access checks are disabled, any code can
use the &#96;java.lang.reflect.Constructor&#96;,
&#96;java.lang.reflect.Method&#96;, or &#96;java.lang.reflect.Field&#96;
object to access the underlying Java entity, without further permission
checks. This breaks encapsulation and can undermine the stability of the
virtual machine. (In contrast, without using the
&#96;setAccessible(boolean)&#96; method, this should not happen because
all the language-defined checks still apply.)

This feature should be avoided if possible.

### Java Native Interface (JNI) {#sect-Defensive_Coding-Java-JNI}

The Java Native Interface allows calling from Java code functions
specifically written for this purpose, usually in C or C++.

The transition between the Java world and the C world is not fully
type-checked, and the C code can easily break the Java virtual machine
semantics. Therefore, extra care is needed when using this
functionality.

To provide a moderate amount of type safety, it is recommended to
recreate the class-specific header file using
\[application\]&#42;javah&#42; during the build process, include it in
the implementation, and use the
\[option\]&#96;-Wmissing-declarations&#96; option.

Ideally, the required data is directly passed to static JNI methods and
returned from them, and the code and the C side does not have to deal
with accessing Java fields (or even methods).

When using &#96;GetPrimitiveArrayCritical&#96; or
&#96;GetStringCritical&#96;, make sure that you only perform very little
processing between the get and release operations. Do not access the
file system or the network, and not perform locking, because that might
introduce blocking. When processing large strings or arrays, consider
splitting the computation into multiple sub-chunks, so that you do not
prevent the JVM from reaching a safepoint for extended periods of time.

If necessary, you can use the Java &#96;long&#96; type to store a C
pointer in a field of a Java class. On the C side, when casting between
the &#96;jlong&#96; value and the pointer on the C side,

You should not try to perform pointer arithmetic on the Java side (that
is, you should treat pointer-carrying &#96;long&#96; values as opaque).
When passing a slice of an array to the native code, follow the Java
convention and pass it as the base array, the integer offset of the
start of the slice, and the integer length of the slice. On the native
side, check the offset/length combination against the actual array
length, and use the offset to compute the pointer to the beginning of
the array.

:::: {#ex-Defensive_Coding-Java-JNI-Pointers .example}
::: title
Array length checking in JNI code
:::

``` java
```
::::

In any case, classes referring to native resources must be declared
&#96;final&#96;, and must not be serializeable or clonable.
Initialization and mutation of the state used by the native side must be
controlled carefully. Otherwise, it might be possible to create an
object with inconsistent native state which results in a crash (or
worse) when used (or perhaps only finalized) later. If you need both
Java inheritance and native resources, you should consider moving the
native state to a separate class, and only keep a reference to objects
of that class. This way, cloning and serialization issues can be avoided
in most cases.

If there are native resources associated with an object, the class
should have an explicit resource deallocation method
(&lt;&lt;sect-Defensive_Coding-Java-Language-Resources&gt;&gt;) and a
finalizer
(&lt;&lt;sect-Defensive_Coding-Java-Language-Finalizers&gt;&gt;) as a
last resort. The need for finalization means that a minimum amount of
synchronization is needed. Code on the native side should check that the
object is not in a closed/freed state.

Many JNI functions create local references. By default, these persist
until the JNI-implemented method returns. If you create many such
references (e.g., in a loop), you may have to free them using
&#96;DeleteLocalRef&#96;, or start using &#96;PushLocalFrame&#96; and
&#96;PopLocalFrame&#96;. Global references must be deallocated with
&#96;DeleteGlobalRef&#96;, otherwise there will be a memory leak, just
as with &#96;malloc&#96; and &#96;free&#96;.

When throwing exceptions using &#96;Throw&#96; or &#96;ThrowNew&#96;, be
aware that these functions return regularly. You have to return control
manually to the JVM.

Technically, the &#96;JNIEnv&#96; pointer is not necessarily constant
during the lifetime of your JNI module. Storing it in a global variable
is therefore incorrect. Particularly if you are dealing with callbacks,
you may have to store the pointer in a thread-local variable (defined
with &#96;+\_\_thread+&#96;). It is, however, best to avoid the
complexity of calling back into Java code.

Keep in mind that C/C and Java are different languages, despite very
similar syntax for expressions. The Java memory model is much more
strict than the C or C memory models, and native code needs more
synchronization, usually using JVM facilities or POSIX threads mutexes.
Integer overflow in Java is defined, but in C/C++ it is not (for the
&#96;jint&#96; and &#96;jlong&#96; types).

### &#96;sun.misc.Unsafe&#96; {#sect-Defensive_Coding-Java-MiscUnsafe}

The &#96;sun.misc.Unsafe&#96; class is unportable and contains many
functions explicitly designed to break Java memory safety (for
performance and debugging). If possible, avoid using this class.

## Interacting with the Security Manager {#sect-Defensive_Coding-Java-SecurityManager}

The Java platform is largely implemented in the Java language itself.
Therefore, within the same JVM, code runs which is part of the Java
installation and which is trusted, but there might also be code which
comes from untrusted sources and is restricted by the Java sandbox (to
varying degrees). The &#42;security manager&#42; draws a line between
fully trusted, partially trusted and untrusted code.

The type safety and accessibility checks provided by the Java language
and JVM would be sufficient to implement a sandbox. However, only some
Java APIs employ such a capabilities-based approach. (The Java SE
library contains many public classes with public constructors which can
break any security policy, such as &#96;java.io.FileOutputStream&#96;.)
Instead, critical functionality is protected by &#42;stack
inspection&#42;: At a security check, the stack is walked from top
(most-nested) to bottom. The security check fails if a stack frame for a
method is encountered whose class lacks the permission which the
security check requires.

This simple approach would not allow untrusted code (which lacks certain
permissions) to call into trusted code while the latter retains trust.
Such trust transitions are desirable because they enable Java as an
implementation language for most parts of the Java platform, including
security-relevant code. Therefore, there is a mechanism to mark certain
stack frames as trusted
(&lt;&lt;sect-Defensive_Coding-Java-SecurityManager-Privileged&gt;&gt;).

In theory, it is possible to run a Java virtual machine with a security
manager that acts very differently from this approach, but a lot of code
expects behavior very close to the platform default (including many
classes which are part of the OpenJDK implementation).

### Security Manager Compatibility {#sect-Defensive_Coding-Java-SecurityManager-Compatible}

A lot of code can run without any additional permissions at all, with
little changes. The following guidelines should help to increase
compatibility with a restrictive security manager.

&#42; When retrieving system properties using
&#96;System.getProperty(String)&#96; or similar methods, catch
&#96;SecurityException&#96; exceptions and treat the property as unset.

&#42; Avoid unnecessary file system or network access.

&#42; Avoid explicit class loading. Access to a suitable class loader
might not be available when executing as untrusted code.

If the functionality you are implementing absolutely requires privileged
access and this functionality has to be used from untrusted code
(hopefully in a restricted and secure manner), see
&lt;&lt;sect-Defensive_Coding-Java-SecurityManager-Privileged&gt;&gt;.

### Activating the Security Manager {#sect-Defensive_Coding-Java-SecurityManager-Activate}

The usual command to launch a Java application,
\[command\]&#96;java&#96;, does not activate the security manager.
Therefore, the virtual machine does not enforce any sandboxing
restrictions, even if explicitly requested by the code (for example, as
described in
&lt;&lt;sect-Defensive_Coding-Java-SecurityManager-Unprivileged&gt;&gt;).

The \[option\]&#96;-Djava.security.manager&#96; option activates the
security manager, with the fairly restrictive default policy. With a
very permissive policy, most Java code will run unchanged. Assuming the
policy in
&lt;&lt;ex-Defensive_Coding-Java-SecurityManager-GrantAll&gt;&gt; has
been saved in a file &#96;grant-all.policy&#96;, this policy can be
activated using the option
\[option\]&#96;-Djava.security.policy=grant-all.policy&#96; (in addition
to the \[option\]&#96;-Djava.security.manager&#96; option).

:::: {#ex-Defensive_Coding-Java-SecurityManager-GrantAll .example}
::: title
Most permissve OpenJDK policy file
:::

``` java
grant {
permission java.security.AllPermission;
};
```
::::

With this most permissive policy, the security manager is still active,
and explicit requests to drop privileges will be honored.

### Reducing Trust in Code {#sect-Defensive_Coding-Java-SecurityManager-Unprivileged}

The
&lt;&lt;ex-Defensive_Coding-Java-SecurityManager-Unprivileged&gt;&gt;
example shows how to run a piece code of with reduced privileges.

:::: {#ex-Defensive_Coding-Java-SecurityManager-Unprivileged .example}
::: title
Using the security manager to run code with reduced privileges
:::

``` java
```
::::

The example above does not add any additional permissions to the
&#96;permissions&#96; object. If such permissions are necessary, code
like the following (which grants read permission on all files in the
current directory) can be used:

``` java
```

:::: important
::: title
:::

Calls to the &#96;java.security.AccessController.doPrivileged()&#96;
methods do not enforce any additional restriction if no security manager
has been set. Except for a few special exceptions, the restrictions no
longer apply if the &#96;doPrivileged()&#96; has returned, even to
objects created by the code which ran with reduced privileges. (This
applies to object finalization in particular.)

The example code above does not prevent the called code from calling the
&#96;java.security.AccessController.doPrivileged()&#96; methods. This
mechanism should be considered an additional safety net, but it still
can be used to prevent unexpected behavior of trusted code. As long as
the executed code is not dynamic and came with the original application
or library, the sandbox is fairly effective.

The &#96;context&#96; argument in
&lt;&lt;ex-Defensive_Coding-Java-SecurityManager-Unprivileged&gt;&gt; is
extremely important---otherwise, this code would increase privileges
instead of reducing them.
::::

For activating the security manager, see
&lt;&lt;sect-Defensive_Coding-Java-SecurityManager-Activate&gt;&gt;.
Unfortunately, this affects the virtual machine as a whole, so it is not
possible to do this from a library.

### Re-gaining Privileges {#sect-Defensive_Coding-Java-SecurityManager-Privileged}

Ordinarily, when trusted code is called from untrusted code, it loses
its privileges (because of the untrusted stack frames visible to stack
inspection). The &#96;java.security.AccessController.doPrivileged()&#96;
family of methods provides a controlled backdoor from untrusted to
trusted code.

:::: important
::: title
:::

By design, this feature can undermine the Java security model and the
sandbox. It has to be used very carefully. Most sandbox vulnerabilities
can be traced back to its misuse.
::::

In essence, the &#96;doPrivileged()&#96; methods cause the stack
inspection to end at their call site. Untrusted code further down the
call stack becomes invisible to security checks.

The following operations are common and safe to perform with elevated
privileges.

&#42; Reading custom system properties with fixed names, especially if
the value is not propagated to untrusted code. (File system paths
including installation paths, host names and user names are sometimes
considered private information and need to be protected.)

&#42; Reading from the file system at fixed paths, either determined at
compile time or by a system property. Again, leaking the file contents
to the caller can be problematic.

&#42; Accessing network resources under a fixed address, name or URL,
derived from a system property or configuration file, information leaks
not withstanding.

The &lt;&lt;ex-Defensive_Coding-Java-SecurityManager-Privileged&gt;&gt;
example shows how to request additional privileges.

:::: {#ex-Defensive_Coding-Java-SecurityManager-Privileged .example}
::: title
Using the security manager to run code with increased privileges
:::

``` java
```
::::

Obviously, this only works if the class containing the call to
&#96;doPrivileged()&#96; is marked trusted (usually because it is loaded
from a trusted class loader).

When writing code that runs with elevated privileges, make sure that you
follow the rules below.

&#42; Make the privileged code as small as possible. Perform as many
computations as possible before and after the privileged code section,
even if it means that you have to define a new class to pass the data
around.

&#42; Make sure that you either control the inputs to the privileged
code, or that the inputs are harmless and cannot affect security
properties of the privileged code.

&#42; Data that is returned from or written by the privileged code must
either be restricted (that is, it cannot be accessed by untrusted code),
or must be harmless. Otherwise, privacy leaks or information disclosures
which affect security properties can be the result.

If the code calls back into untrusted code at a later stage (or performs
other actions under control from the untrusted caller), you must obtain
the original security context and restore it before performing the
callback, as in
&lt;&lt;ex-Defensive_Coding-Java-SecurityManager-Callback&gt;&gt;. (In
this example, it would be much better to move the callback invocation
out of the privileged code section, of course.)

:::: {#ex-Defensive_Coding-Java-SecurityManager-Callback .example}
::: title
Restoring privileges when invoking callbacks
:::

``` java
```
::::

# The Python Programming Language {#_the_python_programming_language}

Python provides memory safety by default, so low-level security
vulnerabilities are rare and typically needs fixing the Python
interpreter or standard library itself.

Other sections with Python-specific advice include:

&#42; [Dealing with temp
files](tasks/Tasks-Temporary_Files.adoc&#35;chap-Defensive_Coding-Tasks-Temporary_Files)

&#42; [Creating Safe
Processes](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-Processes-Creation)

&#42; [Serialization and
Deserialization](tasks/Tasks-Serialization.adoc&#35;chap-Defensive_Coding-Tasks-Serialization),
in particular [Library Support for
Deserialization](tasks/Tasks-Serialization.adoc&#35;sect-Defensive_Coding-Tasks-Serialization-Library)

&#42;
[Randomness](tasks/Tasks-Cryptography.adoc&#35;sect-Defensive_Coding-Tasks-Cryptography-Randomness)

## Dangerous Standard Library Features {#_dangerous_standard_library_features}

Some areas of the standard library, notably the &#96;ctypes&#96; module,
do not provide memory safety guarantees comparable to the rest of
Python. If such functionality is used, the advice in [Defensive Coding
in C](programming-languages/C.adoc&#35;chap-Defensive_Coding-C) should
be followed.

## Run-time Compilation and Code Generation {#_run_time_compilation_and_code_generation}

The following Python functions and statements related to code execution
should be avoided:

&#42; &#96;compile&#96;

&#42; &#96;eval&#96;

&#42; &#96;exec&#96;

&#42; &#96;execfile&#96;

If you need to parse integers or floating point values, use the
&#96;int&#96; and &#96;float&#96; functions instead of &#96;eval&#96;.
Sandboxing untrusted Python code does not work reliably.

## Sandboxing {#_sandboxing}

The &#96;rexec&#96; Python module cannot safely sandbox untrusted code
and should not be used. The standard CPython implementation is not
suitable for sandboxing.

# Shell Programming and \[application\]&#42;bash&#42; {#_shell_programming_and_application42bash42}

This chapter contains advice about shell programming, specifically in
\[application\]&#42;bash&#42;. Most of the advice will apply to scripts
written for other shells because extensions such as integer or array
variables have been implemented there as well, with comparable syntax.

## Consider Alternatives {#sect-Defensive_Coding-Shell-Alternatives}

Once a shell script is so complex that advice in this chapter applies,
it is time to step back and consider the question: Is there a more
suitable implementation language available?

For example, Python with its &#96;subprocess&#96; module can be used to
write scripts which are almost as concise as shell scripts when it comes
to invoking external programs, and Python offers richer data structures,
with less arcane syntax and more consistent behavior.

## Shell Language Features {#sect-Defensive_Coding-Shell-Language}

The following sections cover subtleties concerning the shell programming
languages. They have been written with the \[application\]&#42;bash&#42;
shell in mind, but some of these features apply to other shells as well.

Some of the features described may seem like implementation defects, but
these features have been replicated across multiple independent
implementations, so they now have to be considered part of the shell
programming language.

### Parameter Expansion {#sect-Defensive_Coding-Shell-Parameter_Expansion}

The mechanism by which named shell variables and parameters are expanded
is called &#42;parameter expansion&#42;. The most basic syntax is
"&#96;\$&#96;&#42;variable&#42;" or
"&#96;\${&#96;&#42;variable&#42;&#96;}&#96;".

In almost all cases, a parameter expansion should be enclosed in double
quotation marks &#96;\'&#96;...&#96;\'&#96;.

``` bash
external-program '$arg1' '$arg2'
```

If the double quotation marks are omitted, the value of the variable
will be split according to the current value of the &#96;IFS&#96;
variable. This may allow the injection of additional options which are
then processed by &#96;external-program&#96;.

Parameter expansion can use special syntax for specific features, such
as substituting defaults or performing string or array operations. These
constructs should not be used because they can trigger arithmetic
evaluation, which can result in code execution. See
&lt;&lt;sect-Defensive_Coding-Shell-Arithmetic&gt;&gt;.

### Double Expansion {#sect-Defensive_Coding-Shell-Double_Expansion}

&#42;Double expansion&#42; occurs when, during the expansion of a shell
variable, not just the variable is expanded, replacing it by its value,
but the &#42;value&#42; of the variable is itself is expanded as well.
This can trigger arbitrary code execution, unless the value of the
variable is verified against a restrictive pattern.

The evaluation process is in fact recursive, so a self-referential
expression can cause an out-of-memory condition and a shell crash.

Double expansion may seem like as a defect, but it is implemented by
many shells, and has to be considered an integral part of the shell
programming language. However, it does make writing robust shell scripts
difficult.

Double expansion can be requested explicitly with the &#96;eval&#96;
built-in command, or by invoking a subshell with "&#96;bash -c&#96;".
These constructs should not be used.

The following sections give examples of places where implicit double
expansion occurs.

#### Arithmetic Evaluation {#sect-Defensive_Coding-Shell-Arithmetic}

&#42;Arithmetic evaluation&#42; is a process by which the shell computes
the integer value of an expression specified as a string. It is highly
problematic for two reasons: It triggers double expansion (see
&lt;&lt;sect-Defensive_Coding-Shell-Double_Expansion&gt;&gt;), and the
language of arithmetic expressions is not self-contained. Some
constructs in arithmetic expressions (notably array subscripts) provide
a trapdoor from the restricted language of arithmetic expressions to the
full shell language, thus paving the way towards arbitrary code
execution. Due to double expansion, input which is (indirectly)
referenced from an arithmetic expression can trigger execution of
arbitrary code, which is potentially harmful.

Arithmetic evaluation is triggered by the follow constructs:

&#42; The &#42;expression&#42; in "&#96;\$[]{.indexterm
primary="&#96;&#42;expression&#42;&#96;"}&#96;&#42;expression&#42;&#96;&#96;"
is evaluated. This construct is called &#42;arithmetic expansion&#42;.

&#42;

\+ "&#96;\$\[&#96;&#42;expression&#42;&#96;\]&#96;" is a deprecated
syntax with the same effect.

&#42; The arguments to the &#96;let&#96; shell built-in are evaluated.

&#42;

\+ "&#96;[]{.indexterm
primary="&#96;&#42;expression&#42;&#96;"}&#96;&#42;expression&#42;&#96;&#96;"
is an alternative syntax for "&#96;let&#96; &#42;expression&#42;".

&#42; Conditional expressions surrounded by
"&#96;\[\[&#96;...&#96;\]\]&#96;" can trigger arithmetic evaluation if
certain operators such as &#96;-eq&#96; are used. (The &#96;test&#96;
built-in does not perform arithmetic evaluation, even with integer
operators such as &#96;-eq&#96;.)

\+ The conditional expression "&#96;\[\[ \$&#96;&#42;variable&#42;
&#96;=\~&#96; &#42;regexp&#42; &#96;\]\]&#96;" can be used for input
validation, assuming that &#42;regexp&#42; is a constant regular
expression. See
&lt;&lt;sect-Defensive_Coding-Shell-Input_Validation&gt;&gt;.

&#42; Certain parameter expansions, for example
"&#96;\${&#96;&#42;variable&#42;&#96;\[&#96;&#42;expression&#42;&#96;\]}&#96;"
(array indexing) or
"&#96;\${&#96;&#42;variable&#42;&#96;:&#96;&#42;expression&#42;&#96;}&#96;"
(string slicing), trigger arithmetic evaluation of &#42;expression&#42;.

&#42; Assignment to array elements using
"&#42;array_variable&#42;&#96;\[&#96;&#42;subscript&#42;&#96;\]=&#96;&#42;expression&#42;"
triggers evaluation of &#42;subscript&#42;, but not
&#42;expression&#42;.

&#42; The expressions in the arithmetic &#96;for&#96; command, "&#96;for
[]{.indexterm
primary="&#96;&#42;expression1&#42;&#96;;&#96; &#42;expression2&#42;&#96;;&#96; &#42;expression3&#42;&#96;"}&#96;&#42;expression1&#42;&#96;;&#96;
&#42;expression2&#42;&#96;;&#96; &#42;expression3&#42;&#96;; do&#96;
&#42;commands&#42;&#96;; done&#96;" are evaluated. This does not apply
to the regular for command, "&#96;for&#96; &#42;variable&#42;
&#96;in&#96; &#42;list&#42;&#96;; do&#96; &#42;commands&#42;&#96;;
done&#96;".

:::: important
::: title
:::

Depending on the \[application\]&#42;bash&#42; version, the above list
may be incomplete.

If faced with a situation where using such shell features appears
necessary, see &lt;&lt;sect-Defensive_Coding-Shell-Alternatives&gt;&gt;.
::::

If it is impossible to avoid shell arithmetic on untrusted inputs, refer
to &lt;&lt;sect-Defensive_Coding-Shell-Input_Validation&gt;&gt;.

#### Type declarations {#sect-Defensive_Coding-Shell-Types}

\[application\]&#42;bash&#42; supports explicit type declarations for
shell variables:

``` bash
declare -i integer_variable
declare -a array_variable
declare -A assoc_array_variable

typeset -i integer_variable
typeset -a array_variable
typeset -A assoc_array_variable

local -i integer_variable
local -a array_variable
local -A assoc_array_variable

readonly -i integer_variable
readonly -a array_variable
readonly -A assoc_array_variable
```

Variables can also be declared as arrays by assigning them an array
expression, as in:

``` bash
array_variable=(1 2 3 4)
```

Some built-ins (such as &#96;mapfile&#96;) can implicitly create array
variables.

Such type declarations should not be used because assignment to such
variables (independent of the concrete syntax used for the assignment)
triggers arithmetic expansion (and thus double expansion) of the
right-hand side of the assignment operation. See
&lt;&lt;sect-Defensive_Coding-Shell-Arithmetic&gt;&gt;.

Shell scripts which use integer or array variables should be rewritten
in another, more suitable language. See
&lt;&lt;sect-Defensive_Coding-Shell-Alternatives&gt;&gt;.

### Other Obscurities {#sect-Defensive_Coding-Shell-Obscure}

Obscure shell language features should not be used. Examples are:

&#42; Exported functions (&#96;export -f&#96; or &#96;declare -f&#96;).

&#42; Function names which are not valid variable names, such as
"&#96;module::function&#96;".

&#42; The possibility to override built-ins or external commands with
shell functions.

&#42; Changing the value of the &#96;IFS&#96; variable to tokenize
strings.

## Invoking External Commands {#sect-Defensive_Coding-Shell-Invoke}

When passing shell variables as single command line arguments, they
should always be surrounded by double quotes. See
&lt;&lt;sect-Defensive_Coding-Shell-Parameter_Expansion&gt;&gt;.

Care is required when passing untrusted values as positional parameters
to external commands. If the value starts with a hyphen "&#96;-&#96;",
it may be interpreted by the external command as an option. Depending on
the external program, a "&#96;\--&#96;" argument stops option processing
and treats all following arguments as positional parameters. (Double
quotes are completely invisible to the command being invoked, so they do
not prevent variable values from being interpreted as options.)

Cleaning the environment before invoking child processes is difficult to
implement in script. \[application\]&#42;bash&#42; keeps a hidden list
of environment variables which do not correspond to shell variables, and
unsetting them from within a \[application\]&#42;bash&#42; script is not
possible. To reset the environment, a script can re-run itself under the
"&#96;env -i&#96;" command with an additional parameter which indicates
the environment has been cleared and suppresses a further
self-execution. Alternatively, individual commands can be executed with
"&#96;env -i&#96;".

:::: important
::: title
:::

Complete isolation from its original execution environment (which is
required when the script is executed after a trust transition, e.g.,
triggered by the SUID mechanism) is impossible to achieve from within
the shell script itself. Instead, the invoking process has to clear the
process environment (except for few trusted variables) before running
the shell script.
::::

Checking for failures in executed external commands is recommended. If
no elaborate error recovery is needed, invoking "&#96;set -e&#96;" may
be sufficient. This causes the script to stop on the first failed
command. However, failures in pipes ("&#96;command1 \| command2&#96;")
are only detected for the last command in the pipe, errors in previous
commands are ignored. This can be changed by invoking "&#96;set -o
pipefail&#96;". Alternatively, return codes for previous commands in
pipes can be accessed in the ("&#96;\${PIPESTATUS\[X\]}&#96;") array.
Due to architectural limitations, only the process that spawned the
entire pipe can check for failures in individual commands; it is not
possible for a process to tell if the process feeding data (or the
process consuming data) exited normally or with an error.

See [Creating Safe
Processes](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-Processes-Creation)
for additional details on creating child processes.

## Temporary Files {#sect-Defensive_Coding-Shell-Temporary_Files}

Temporary files should be created with the &#96;mktemp&#96; command, and
temporary directories with "&#96;mktemp -d&#96;".

To clean up temporary files and directories, write a clean-up shell
function and register it as a trap handler, as shown in
&lt;&lt;ex-Defensive_Coding-Tasks-Temporary_Files&gt;&gt;. Using a
separate function avoids issues with proper quoting of variables.

:::: {#ex-Defensive_Coding-Tasks-Temporary_Files .example}
::: title
Creating and Cleaning up Temporary Files
:::

``` bash
tmpfile='$(mktemp)'

cleanup () {
rm -f -- '$tmpfile'
}

trap cleanup 0
```
::::

## Performing Input Validation {#sect-Defensive_Coding-Shell-Input_Validation}

In some cases, input validation cannot be avoided. For example, if
arithmetic evaluation is absolutely required, it is imperative to check
that input values are, in fact, integers. See
&lt;&lt;sect-Defensive_Coding-Shell-Arithmetic&gt;&gt;.

&lt;&lt;ex-Defensive_Coding-Shell-Input_Validation&gt;&gt; shows a
construct which can be used to check if a string "&#96;\$value&#96;" is
an integer. This construct is specific to \[application\]&#42;bash&#42;
and not portable to POSIX shells.

:::: {#ex-Defensive_Coding-Shell-Input_Validation .example}
::: title
Input validation in \[application\]&#42;bash&#42;
:::

``` bash
```
::::

Using &#96;case&#96; statements for input validation is also possible
and supported by other (POSIX) shells, but the pattern language is more
restrictive, and it can be difficult to write suitable patterns.

The &#96;expr&#96; external command can give misleading results (e.g.,
if the value being checked contains operators itself) and should not be
used.

## Guarding Shell Scripts Against Changes {#sect-Defensive_Coding-Shell-Edit_Guard}

\[application\]&#42;bash&#42; only reads a shell script up to the point
it is needed for executed the next command. This means that if script is
overwritten while it is running, execution can jump to a random part of
the script, depending on what is modified in the script and how the file
offsets change as a result. (This behavior is needed to support
self-extracting shell archives whose script part is followed by a stream
of bytes which does not follow the shell language syntax.)

Therefore, long-running scripts should be guarded against concurrent
modification by putting as much of the program logic into a
&#96;main&#96; function, and invoking the &#96;main&#96; function at the
end of the script, using this syntax:

``` bash
main '$@' ; exit $?
```

This construct ensures that \[application\]&#42;bash&#42; will stop
execution after the &#96;main&#96; function, instead of opening the
script file and trying to read more commands.

# The Go Programming Language {#_the_go_programming_language}

This chapter contains language-specific recommendations for Go.

## Memory Safety {#chap-Defensive_Coding-Go-Memory_Safety}

Go provides memory safety, but only if the program is not executed in
parallel (that is, &#96;GOMAXPROCS&#96; is not larger than &#96;1&#96;).
The reason is that interface values and slices consist of multiple words
are not updated atomically. Another thread of execution can observe an
inconsistent pairing between type information and stored value (for
interfaces) or pointer and length (for slices), and such inconsistency
can lead to a memory safety violation.

Code which does not run in parallel and does not use the
&#96;unsafe&#96; package (or other packages which expose unsafe
constructs) is memory-safe. For example, invalid casts and out-of-range
subscripting cause panics at run time.

Keep in mind that finalization can introduce parallelism because
finalizers are executed concurrently, potentially interleaved with the
rest of the program.

## Error Handling {#chap-Defensive_Coding-Go-Error_Handling}

Only a few common operations (such as pointer dereference, integer
division, array subscripting) trigger exceptions in Go, called
&#42;panics&#42;. Most interfaces in the standard library use a separate
return value of type &#96;error&#96; to signal error.

Not checking error return values can lead to incorrect operation and
data loss (especially in the case of writes, using interfaces such as
&#96;io.Writer&#96;).

The correct way to check error return values depends on the function or
method being called. In the majority of cases, the first step after
calling a function should be an error check against the &#96;nil&#96;
value, handling any encountered error. See
&lt;&lt;ex-Defensive_Coding-Go-Error_Handling-Regular&gt;&gt; for
details.

:::: {#ex-Defensive_Coding-Go-Error_Handling-Regular .example}
::: title
Regular error handling in Go
:::

``` go
```
::::

However, with &#96;io.Reader&#96;, &#96;io.ReaderAt&#96; and related
interfaces, it is necessary to check for a non-zero number of read bytes
first, as shown in
&lt;&lt;ex-Defensive_Coding-Go-Error_Handling-IO&gt;&gt;. If this
pattern is not followed, data loss may occur. This is due to the fact
that the &#96;io.Reader&#96; interface permits returning both data and
an error at the same time.

:::: {#ex-Defensive_Coding-Go-Error_Handling-IO .example}
::: title
Read error handling in Go
:::

``` go
```
::::

## Garbage Collector {#chap-Defensive_Coding-Go-Garbage_Collector}

Older Go releases (before Go 1.3) use a conservative garbage collector
without blacklisting. This means that data blobs can cause retention of
unrelated data structures because the data is conservatively interpreted
as pointers. This phenomenon can be triggered accidentally on 32-bit
architectures and is more likely to occur if the heap grows larger. On
64-bit architectures, it may be possible to trigger it deliberately---it
is unlikely to occur spontaneously.

## Marshaling and Unmarshaling {#chap-Defensive_Coding-Go-Marshaling}

Several packages in the &#96;encoding&#96; hierarchy provide support for
serialization and deserialization. The usual caveats apply (see
[Serialization and Deserialization](tasks/Tasks-Serialization.xml)).

As an additional precaution, the &#96;Unmarshal&#96; and
&#96;Decode&#96; functions should only be used with fresh values in the
&#96;interface{}&#96; argument. This is due to the way defaults for
missing values are implemented: During deserialization, missing value do
not result in an error, but the original value is preserved. Using a
fresh value (with suitable default values if necessary) ensures that
data from a previous deserialization operation does not leak into the
current one. This is especially relevant when structs are deserialized.

## Good Practices for Securing Go - High Level Overview {#chap-Defensive_Coding-Go-Marshaling}

Secure coding is the practice of writing programs that are resistant to
attack by malicious or mischievous people or programs.

Golang's adoption has been increasing over the years. Projects within
Red Hat like
[&#42;Operators&#42;](https://cloud.redhat.com/learn/topics/operators/)
and [&#42;Terraform&#42;](https://www.terraform.io/) have been completed
in this programming language.

### 1. Use Go Modules {#_1_use_go_modules}

Modules are how Go manages dependencies. [&#42;Go
Modules&#42;](https://go.dev/ref/mod/) allow for dependency version
pinning, including transitive modules, and also provides assurance
against unexpected module mutation via the go.sum checksum database.

For an introduction to creating Go projects, see [&#42;How to Write Go
Code&#42;](https://go.dev/doc/code/). For information on using modules,
migrating projects to modules, and other topics, see the blog series
starting with [&#42;Using Go
Modules&#42;](https://go.dev/blog/using-go-modules).

### 2. Validate input entries {#_2_validate_input_entries}

Helps avoid attackers who send us intrusive data that could damage the
system.

To validate user input, you can use native Go packages like strconv to
handle string conversions to other data types. Go also has support for
regular expressions with regexp for complex validations. Even though
Go's preference is to use native libraries, there are third-party
packages like
[&#42;validator&#42;](https://github.com/go-playground/validator/). With
validator, you can include validations for structs or individual fields
more easily.

### 3. Use HTML templates {#_3_use_html_templates}

One critical and common vulnerability is cross-site scripting or XSS.
This exploit consists basically of the attacker being able to inject
malicious code into the app to modify the output.

Go has the package
[&#42;html/template&#42;](https://pkg.go.dev/html/template) to encode
what the app will return to the user. So, instead of the browser
executing an input like &lt;script&gt;alert('You've Been
Hacked!');&lt;/script&gt;, popping up an alert message; you could encode
the input, and the app will treat the input as a typical HTML code
printed in the browser.

There are also third-party libraries you can use when developing web
apps in Go. For example, there's [&#42;Gorilla web
toolkit&#42;](https://www.gorillatoolkit.org/), which includes libraries
to help developers to do things like encoding authentication cookie
values. There's also
[&#42;nosurf&#42;](https://github.com/justinas/nosurf/), which is an
HTTP package that helps with the prevention of cross-site request
forgery
([&#42;CSRF&#42;](https://owasp.org/www-community/attacks/csrf/)).

``` _go
name := r.FormValue('name')
template := template.Must(template.ParseGlob('xss.html'))
data['Name'] = name
err := template.ExecuteTemplate(w, name, data)
```

### 4. Protect yourself from SQL injections {#_4_protect_yourself_from_sql_injections}

The first thing you need you to do is make sure a user that connects to
the database has limited permissions. A good practice is to also
sanitize the user's input, as I described in a previous section, or to
escape special characters and use
[&#42;HTMLEscapeString&#42;](https://pkg.go.dev/html/template&#35;HTMLEscapeString/)
function from the HTML template package. But, the most critical piece of
code you'd need to include is the use of parameterized queries. In Go,
you don't prepare a statement in a connection; you prepare it on the DB.
Here's an example of how to use parameterized queries:

``` _go
customerName := r.URL.Query().Get('name')
db.Exec('UPDATE creditcards SET name=? WHERE customerId=?', customerName, 233, 90)
```

If using the db.Query() function instead, ensure you sanitize the user's
input first, as above.

### 5. Encrypt sensitive information {#_5_encrypt_sensitive_information}

Go package that includes robust implementations to encrypt information
like [&#42;crypto&#42;](https://pkg.go.dev/golang.org/x/crypto/).

### 6. Enforce HTTPS communication {#_6_enforce_https_communication}

To secure in-transit connection in the system isn't only about the app
listening in port 443. You also need to use proper certificates and
enforce HTTPS to avoid attackers downgrading the protocol to HTTP.

``` _go
w.Header().Add('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')
```

You might also want to specify the server name in the TLS configuration,
like this:

``` _go
config := \&amp;tls.Config{ServerName: 'yourSiteOrServiceName'}
```

Of Note: It's always a good practice to implement in-transit encryption
even if your application is only for internal communication. Imagine if,
for some reason, an attacker could sniff your internal traffic. Whenever
you can, it's always best to raise the difficulty bar for possible
future attackers.

### 7. Use caution with unsafe and cgo {#_7_use_caution_with_unsafe_and_cgo}

Package [&#42;unsafe&#42;](https://pkg.go.dev/unsafe) provides an escape
hatch from Go's type system, enabling interactions with low-level and
system call APIs, in a manner similar to C programs. However, unsafe has
several rules which must be followed in order to perform these
interactions in a sane way. It's easy to make [&#42;subtle mistakes when
writing unsafe
code&#42;](https://github.com/golang/sys/commit/b69606af412f43a225c1cf2044c90e317f41ae09/),
but these mistakes can often be avoided. This blog post:
[&#42;Safe-use-of-unsafe-pointer&#42;](https://blog.gopheracademy.com/advent-2019/safe-use-of-unsafe-pointer/)
will introduce some of the current and upcoming Go tooling that can
verify safe usage of the unsafe. Pointer type in your Go programs. If
you have not worked with unsafe before, Recommended reading previous
[&#42;Gopher Academy Advent series
blog&#42;](https://blog.gopheracademy.com/advent-2017/unsafe-pointer-and-system-calls/)
on the topic.

Go's [&#42;cgo&#42;](https://pkg.go.dev/cmd/cgo) system for calling C
functions offers a very convenient feature. As outlined in
<https://relistan.com/cgo-when-and-when-not-to-use-it>

Here are some problems with using Cgo in your application:

&#42; It breaks a lot of Go's awesome tooling &#42; Puts Go's
concurrency promise at risk &#42; Might break your static binary, &#42;
Breaks cross-compiling almost always &#42; Calls into Cgo are much
slower than native Go calls

### 8. Be mindful with Errors and Logs {#_8_be_mindful_with_errors_and_logs}

Go doesn't have exceptions. This means that you'd need to handle errors
differently than with other languages. The standard looks like this:

``` _go
if err != nil {
// handle the error
}
```

Also, Go offers a native library to work with logs. The most simple code
is like this:

``` _go
package main

import (
'log'
)

func main() {
log.Print('Logging in Go!')
}
```

Finally, make sure you apply all the previous rules like encryption and
sanitization of the data you put into the logs.

#### Libraries {#_libraries}

&#42; [&#42;paseto - Platform-Agnostic Security Tokens implementation in
GO (Golang)&#42;](https://github.com/o1egl/paseto) &#42; [&#42;hsts - Go
HTTP Strict Transport Security
library&#42;](https://github.com/StalkR/hsts/) &#42; [&#42;jwt-go -
Golang implementation of JSON Web Tokens
(JWT)&#42;](https://github.com/dgrijalva/jwt-go/)

#### Further Reading {#_further_reading}

&#42; <https://github.com/Binject/awesome-go-security> &#42;
<https://owasp.org/www-pdf-archive/Owasp-171123063052.pdf> &#42;
<https://github.com/securego/gosec> &#42;
<https://tutorialedge.net/golang/secure-coding-in-go-input-validation/>
&#42; <https://tour.golang.org/list> &#42;
<https://snyk.io/blog/go-security-cheatsheet-for-go-developers/> &#42;
<https://hackernoon.com/security-considerations-in-golang-xo4y3ykk>
&#42; <https://golang.org/security> &#42;
<https://github.com/guardrailsio/awesome-golang-security> &#42;
<https://blog.sqreen.com/top-6-security-best-practices-for-go/> &#42;
<https://cyral.com/blog/security-as-code-implementing-lint-and-gosec/>
&#42; <https://github.com/OWASP/Go-SCP> &#42;
<https://spacetime.dev/memory-security-go> &#42;
<https://github.com/parsiya/Hacking-with-Go> &#42;
<https://github.com/denji/golang-tls> &#42;
<https://checkmarx.com/blog/redos-go/> &#42;
<https://blog.trailofbits.com/2019/11/07/attacking-go-vr-ttps/> &#42;
<https://utcc.utoronto.ca/~cks/space/blog/programming/GoCgoErrorReturns>

# The Vala Programming Language {#_the_vala_programming_language}

Vala is a programming language mainly targeted at GNOME developers.

Its syntax is inspired by C&#35; (and thus, indirectly, by Java). But
unlike C&#35; and Java, Vala does not attempt to provide memory safety:
Vala is compiled to C, and the C code is compiled with GCC using typical
compiler flags. Basic operations like integer arithmetic are directly
mapped to C constructs. As a results, the recommendations in [Defensive
Coding in C](programming-languages/C.adoc&#35;chap-Defensive_Coding-C)
apply.

In particular, the following Vala language constructs can result in
undefined behavior at run time:

&#42; Integer arithmetic, as described in [Recommendations for Integer
Arithmetic](programming-languages/C.adoc&#35;sect-Defensive_Coding-C-Arithmetic).

&#42; Pointer arithmetic, string subscripting and the
&#96;substring&#96; method on strings (the &#96;string&#96; class in the
&#96;glib-2.0&#96; package) are not range-checked. It is the
responsibility of the calling code to ensure that the arguments being
passed are valid. This applies even to cases (like &#96;substring&#96;)
where the implementation would have range information to check the
validity of indexes. See [Recommendations for Pointers and Array
Handling](programming-languages/C.adoc&#35;sect-Defensive_Coding-C-Pointers)

&#42; Similarly, Vala only performs garbage collection (through
reference counting) for &#96;GObject&#96; values. For plain C pointers
(such as strings), the programmer has to ensure that storage is
deallocated once it is no longer needed (to avoid memory leaks), and
that storage is not being deallocated while it is still being used (see
[Use-after-free
errors](programming-languages/C.adoc&#35;sect-Defensive_Coding-C-Use-After-Free)).

&#42; Specific Programming Tasks :experimental: :toc:

# Library Design {#_library_design}

Through this section, the term &#42;client code&#42; refers to
applications and other libraries using the library.

## State Management {#_state_management}

### Global State {#_global_state}

Global state should be avoided.

If this is impossible, the global state must be protected with a lock.
For C/C++, you can use the &#96;pthread_mutex_lock&#96; and
&#96;pthread_mutex_unlock&#96; functions without linking against
&#96;-lpthread&#96; because the system provides stubs for non-threaded
processes.

For compatibility with &#96;fork&#96;, these locks should be acquired
and released in helpers registered with &#96;pthread_atfork&#96;. This
function is not available without &#96;-lpthread&#96;, so you need to
use &#96;dlsym&#96; or a weak symbol to obtain its address.

If you need &#96;fork&#96; protection for other reasons, you should
store the process ID and compare it to the value returned by
&#96;getpid&#96; each time you access the global state.
(&#96;getpid&#96; is not implemented as a system call and is fast.) If
the value changes, you know that you have to re-create the state object.
(This needs to be combined with locking, of course.)

### Handles {#_handles}

Library state should be kept behind a curtain. Client code should
receive only a handle. In C, the handle can be a pointer to an
incomplete &#96;struct&#96;. In C++, the handle can be a pointer to an
abstract base class, or it can be hidden using the
pointer-to-implementation idiom.

The library should provide functions for creating and destroying
handles. (In C++, it is possible to use virtual destructors for the
latter.) Consistency between creation and destruction of handles is
strongly recommended: If the client code created a handle, it is the
responsibility of the client code to destroy it. (This is not always
possible or convenient, so sometimes, a transfer of ownership has to
happen.)

Using handles ensures that it is possible to change the way the library
represents state in a way that is transparent to client code. This is
important to facilitate security updates and many other code changes.

It is not always necessary to protect state behind a handle with a lock.
This depends on the level of thread safety the library provides.

## Object Orientation {#_object_orientation}

Classes should be either designed as base classes, or it should be
impossible to use them as base classes (like &#96;final&#96; classes in
Java). Classes which are not designed for inheritance and are used as
base classes nevertheless create potential maintenance hazards because
it is difficult to predict how client code will react when calls to
virtual methods are added, reordered or removed.

Virtual member functions can be used as callbacks. See
&lt;&lt;sect-Defensive_Coding-Tasks-Library_Design-Callbacks&gt;&gt; for
some of the challenges involved.

## Callbacks {#sect-Defensive_Coding-Tasks-Library_Design-Callbacks}

Higher-order code is difficult to analyze for humans and computers
alike, so it should be avoided. Often, an iterator-based interface (a
library function which is called repeatedly by client code and returns a
stream of events) leads to a better design which is easier to document
and use.

If callbacks are unavoidable, some guidelines for them follow.

In modern C++ code, &#96;std::function&#96; objects should be used for
callbacks.

In older C++ code and in C code, all callbacks must have an additional
closure parameter of type &#96;void &#42;&#96;, the value of which can
be specified by client code. If possible, the value of the closure
parameter should be provided by client code at the same time a specific
callback is registered (or specified as a function argument). If a
single closure parameter is shared by multiple callbacks, flexibility is
greatly reduced, and conflicts between different pieces of client code
using the same library object could be unresolvable. In some cases, it
makes sense to provide a de-registration callback which can be used to
destroy the closure parameter when the callback is no longer used.

Callbacks can throw exceptions or call &#96;longjmp&#96;. If possible,
all library objects should remain in a valid state. (All further
operations on them can fail, but it should be possible to deallocate
them without causing resource leaks.)

The presence of callbacks raises the question if functions provided by
the library are &#42;reentrant&#42;. Unless a library was designed for
such use, bad things will happen if a callback function uses functions
in the same library (particularly if they are invoked on the same
objects and manipulate the same state). When the callback is invoked,
the library can be in an inconsistent state. Reentrant functions are
more difficult to write than thread-safe functions (by definition,
simple locking would immediately lead to deadlocks). It is also
difficult to decide what to do when destruction of an object which is
currently processing a callback is requested.

## Process Attributes {#_process_attributes}

Several attributes are global and affect all code in the process, not
just the library that manipulates them.

&#42; environment variables (see [Accessing Environment
Variables](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-secure_getenv))

&#42; umask

&#42; user IDs, group IDs and capabilities

&#42; current working directory

&#42; signal handlers, signal masks and signal delivery

&#42; file locks (especially &#96;fcntl&#96; locks behave in surprising
ways, not just in a multi-threaded environment)

Library code should avoid manipulating these global process attributes.
It should not rely on environment variables, umask, the current working
directory and signal masks because these attributes can be inherited
from an untrusted source.

In addition, there are obvious process-wide aspects such as the virtual
memory layout, the set of open files and dynamic shared objects, but
with the exception of shared objects, these can be manipulated in a
relatively isolated way.

# File Descriptor Management {#_file_descriptor_management}

File descriptors underlie all input/output mechanisms offered by the
system. They are used to implementation the &#96;FILE &#42;&#96;-based
functions found in &#96;&lt;stdio.h&gt;&#96;, and all the file and
network communication facilities provided by the Python and Java
environments are eventually implemented in them.

File descriptors are small, non-negative integers in userspace, and are
backed on the kernel side with complicated data structures which can
sometimes grow very large.

## Closing Descriptors {#_closing_descriptors}

If a descriptor is no longer used by a program and is not closed
explicitly, its number cannot be reused (which is problematic in itself,
see &lt;&lt;sect-Defensive_Coding-Tasks-Descriptors-Limit&gt;&gt;), and
the kernel resources are not freed. Therefore, it is important to close
all descriptors at the earliest point in time possible, but not earlier.

### Error Handling during Descriptor Close {#_error_handling_during_descriptor_close}

The &#96;close&#96; system call is always successful in the sense that
the passed file descriptor is never valid after the function has been
called. However, &#96;close&#96; still can return an error, for example
if there was a file system failure. But this error is not very useful
because the absence of an error does not mean that all caches have been
emptied and previous writes have been made durable. Programs which need
such guarantees must open files with &#96;O_SYNC&#96; or use
&#96;fsync&#96; or &#96;fdatasync&#96;, and may also have to
&#96;fsync&#96; the directory containing the file.

### Closing Descriptors and Race Conditions {#_closing_descriptors_and_race_conditions}

Unlike process IDs, which are recycle only gradually, the kernel always
allocates the lowest unused file descriptor when a new descriptor is
created. This means that in a multi-threaded program which constantly
opens and closes file descriptors, descriptors are reused very quickly.
Unless descriptor closing and other operations on the same file
descriptor are synchronized (typically, using a mutex), there will be
race conditions and I/O operations will be applied to the wrong file
descriptor.

Sometimes, it is necessary to close a file descriptor concurrently,
while another thread might be about to use it in a system call. In order
to support this, a program needs to create a single special file
descriptor, one on which all I/O operations fail. One way to achieve
this is to use &#96;socketpair&#96;, close one of the descriptors, and
call &#96;shutdown(fd, SHUTRDWR)&#96; on the other.

When a descriptor is closed concurrently, the program does not call
&#96;close&#96; on the descriptor. Instead it program uses
&#96;dup2&#96; to replace the descriptor to be closed with the dummy
descriptor created earlier. This way, the kernel will not reuse the
descriptor, but it will carry out all other steps associated with
calling a descriptor (for instance, if the descriptor refers to a stream
socket, the peer will be notified).

This is just a sketch, and many details are missing. Additional data
structures are needed to determine when it is safe to really close the
descriptor, and proper locking is required for that.

### Lingering State after Close {#_lingering_state_after_close}

By default, closing a stream socket returns immediately, and the kernel
will try to send the data in the background. This means that it is
impossible to implement accurate accounting of network-related resource
utilization from userspace.

The &#96;SO_LINGER&#96; socket option alters the behavior of
&#96;close&#96;, so that it will return only after the lingering data
has been processed, either by sending it to the peer successfully, or by
discarding it after the configured timeout. However, there is no
interface which could perform this operation in the background, so a
separate userspace thread is needed for each &#96;close&#96; call,
causing scalability issues.

Currently, there is no application-level countermeasure which applies
universally. Mitigation is possible with
\[application\]&#42;iptables&#42; (the &#96;connlimit&#96; match type in
particular) and specialized filtering devices for denial-of-service
network traffic.

These problems are not related to the &#96;TIME_WAIT&#96; state commonly
seen in \[application\]&#42;netstat&#42; output. The kernel
automatically expires such sockets if necessary.

## Preventing File Descriptor Leaks to Child Processes {#sect-Defensive_Coding-Tasks-Descriptors-Child_Processes}

Child processes created with &#96;fork&#96; share the initial set of
file descriptors with their parent process. By default, file descriptors
are also preserved if a new process image is created with
&#96;execve&#96; (or any of the other functions such as &#96;system&#96;
or &#96;posix_spawn&#96;).

Usually, this behavior is not desirable. There are two ways to turn it
off, that is, to prevent new process images from inheriting the file
descriptors in the parent process:

&#42; Set the close-on-exec flag on all newly created file descriptors.
Traditionally, this flag is controlled by the &#96;FD_CLOEXEC&#96; flag,
using &#96;F_GETFD&#96; and &#96;F_SETFD&#96; operations of the
&#96;fcntl&#96; function.

\+ However, in a multi-threaded process, there is a race condition: a
subprocess could have been created between the time the descriptor was
created and the &#96;FD_CLOEXEC&#96; was set. Therefore, many system
calls which create descriptors (such as &#96;open&#96; and
&#96;openat&#96;) now accept the &#96;O_CLOEXEC&#96; flag
(&#96;SOCK_CLOEXEC&#96; for &#96;socket&#96; and &#96;socketpair&#96;),
which cause the &#96;FD_CLOEXEC&#96; flag to be set for the file
descriptor in an atomic fashion. In addition, a few new systems calls
were introduced, such as &#96;pipe2&#96; and &#96;dup3&#96;.

\+ The downside of this approach is that every descriptor needs to
receive special treatment at the time of creation, otherwise it is not
completely effective.

&#42; After calling &#96;fork&#96;, but before creating a new process
image with &#96;execve&#96;, all file descriptors which the child
process will not need are closed.

\+ Traditionally, this was implemented as a loop over file descriptors
ranging from &#96;3&#96; to &#96;255&#96; and later &#96;1023&#96;. But
this is only an approximation because it is possible to create file
descriptors outside this range easily (see
&lt;&lt;sect-Defensive_Coding-Tasks-Descriptors-Limit&gt;&gt;). Another
approach reads &#96;/proc/self/fd&#96; and closes the unexpected
descriptors listed there, but this approach is much slower.

At present, environments which care about file descriptor leakage
implement the second approach. OpenJDK 6 and 7 are among them.

## Dealing with the &#96;select&#96; Limit {#sect-Defensive_Coding-Tasks-Descriptors-Limit}

By default, a user is allowed to open only 1024 files in a single
process, but the system administrator can easily change this limit
(which is necessary for busy network servers). However, there is another
restriction which is more difficult to overcome.

The &#96;select&#96; function only supports a maximum of
&#96;FD_SETSIZE&#96; file descriptors (that is, the maximum permitted
value for a file descriptor is &#96;FD_SETSIZE - 1&#96;, usually 1023.)
If a process opens many files, descriptors may exceed such limits. It is
impossible to query such descriptors using &#96;select&#96;.

If a library which creates many file descriptors is used in the same
process as a library which uses &#96;select&#96;, at least one of them
needs to be changed. Calls to &#96;select&#96; can be replaced with
calls to &#96;poll&#96; or another event handling mechanism. Replacing
the &#96;select&#96; function is the recommended approach.

Alternatively, the library with high descriptor usage can relocate
descriptors above the &#96;FD_SETSIZE&#96; limit using the following
procedure.

&#42; Create the file descriptor &#96;fd&#96; as usual, preferably with
the &#96;O_CLOEXEC&#96; flag.

&#42; Before doing anything else with the descriptor &#96;fd&#96;,
invoke:

``` c
int newfd = fcntl(fd, F_DUPFD_CLOEXEC, (long)FD_SETSIZE);
```

&#42; Check that &#96;newfd&#96; result is non-negative, otherwise close
&#96;fd&#96; and report an error, and return.

&#42; Close &#96;fd&#96; and continue to use &#96;newfd&#96;.

The new descriptor has been allocated above the &#96;FD_SETSIZE&#96;.
Even though this algorithm is racy in the sense that the
&#96;FD_SETSIZE&#96; first descriptors could fill up, a very high degree
of physical parallelism is required before this becomes a problem.

# File System Manipulation {#_file_system_manipulation}

In this chapter, we discuss general file system manipulation, with a
focus on access files and directories to which an other, potentially
untrusted user has write access.

Temporary files are covered in their own chapter, [Temporary
Files](tasks/Tasks-Temporary_Files.adoc&#35;chap-Defensive_Coding-Tasks-Temporary_Files).

## Working with Files and Directories Owned by Other Users {#sect-Defensive_Coding-Tasks-File_System-Unowned}

Sometimes, it is necessary to operate on files and directories owned by
other (potentially untrusted) users. For example, a system administrator
could remove the home directory of a user, or a package manager could
update a file in a directory which is owned by an application-specific
user. This differs from accessing the file system as a specific user;
see &lt;&lt;sect-Defensive_Coding-Tasks-File_System-Foreign&gt;&gt;.

Accessing files across trust boundaries faces several challenges,
particularly if an entire directory tree is being traversed:

1.  Another user might add file names to a writable directory at any
    time. This can interfere with file creation and the order of names
    returned by &#96;readdir&#96;.

2.  Merely opening and closing a file can have side effects. For
    instance, an automounter can be triggered, or a tape device rewound.
    Opening a file on a local file system can block indefinitely, due to
    mandatory file locking, unless the &#96;O_NONBLOCK&#96; flag is
    specified.

3.  Hard links and symbolic links can redirect the effect of file system
    operations in unexpected ways. The &#96;O_NOFOLLOW&#96; and
    &#96;AT_SYMLINK_NOFOLLOW&#96; variants of system calls only affected
    final path name component.

4.  The structure of a directory tree can change. For example, the
    parent directory of what used to be a subdirectory within the
    directory tree being processed could suddenly point outside that
    directory tree.

Files should always be created with the &#96;O_CREAT&#96; and
&#96;O_EXCL&#96; flags, so that creating the file will fail if it
already exists. This guards against the unexpected appearance of file
names, either due to creation of a new file, or hard-linking of an
existing file. In multi-threaded programs, rather than manipulating the
umask, create the files with mode &#96;000&#96; if possible, and adjust
it afterwards with &#96;fchmod&#96;.

To avoid issues related to symbolic links and directory tree
restructuring, the "&#96;at&#96;" variants of system calls have to be
used (that is, functions like &#96;openat&#96;, &#96;fchownat&#96;,
&#96;fchmodat&#96;, and &#96;unlinkat&#96;, together with
&#96;O_NOFOLLOW&#96; or &#96;AT_SYMLINK_NOFOLLOW&#96;). Path names
passed to these functions must have just a single component (that is,
without a slash). When descending, the descriptors of parent directories
must be kept open. The missing &#96;opendirat&#96; function can be
emulated with &#96;openat&#96; (with an &#96;O_DIRECTORY&#96; flag, to
avoid opening special files with side effects), followed by
&#96;fdopendir&#96;.

If the "&#96;at&#96;" functions are not available, it is possible to
emulate them by changing the current directory. (Obviously, this only
works if the process is not multi-threaded.) &#96;fchdir&#96; has to be
used to change the current directory, and the descriptors of the parent
directories have to be kept open, just as with the "&#96;at&#96;"-based
approach. &#96;chdir(\'&#8230;\')&#96; is unsafe because it might ascend
outside the intended directory tree.

This "&#96;at&#96;" function emulation is currently required when
manipulating extended attributes. In this case, the &#96;lsetxattr&#96;
function can be used, with a relative path name consisting of a single
component. This also applies to SELinux contexts and the
&#96;lsetfilecon&#96; function.

Currently, it is not possible to avoid opening special files
&#42;and&#42; changes to files with hard links if the directory
containing them is owned by an untrusted user. (Device nodes can be
hard-linked, just as regular files.) &#96;fchmodat&#96; and
&#96;fchownat&#96; affect files whose link count is greater than one.
But opening the files, checking that the link count is one with
&#96;fstat&#96;, and using &#96;fchmod&#96; and &#96;fchown&#96; on the
file descriptor may have unwanted side effects, due to item 2 above.
When creating directories, it is therefore important to change the
ownership and permissions only after it has been fully created. Until
that point, file names are stable, and no files with unexpected hard
links can be introduced.

Similarly, when just reading a directory owned by an untrusted user, it
is currently impossible to reliably avoid opening special files.

There is no workaround against the instability of the file list returned
by &#96;readdir&#96;. Concurrent modification of the directory can
result in a list of files being returned which never actually existed on
disk.

Hard links and symbolic links can be safely deleted using
&#96;unlinkat&#96; without further checks because deletion only affects
the name within the directory tree being processed.

## Accessing the File System as a Different User {#sect-Defensive_Coding-Tasks-File_System-Foreign}

This section deals with access to the file system as a specific user.
This is different from accessing files and directories owned by a
different, potentially untrusted user; see
&lt;&lt;sect-Defensive_Coding-Tasks-File_System-Foreign&gt;&gt;.

One approach is to spawn a child process which runs under the target
user and group IDs (both effective and real IDs). Note that this child
process can block indefinitely, even when processing regular files only.
For example, a special FUSE file system could cause the process to hang
in uninterruptible sleep inside a &#96;stat&#96; system call.

An existing process could change its user and group ID using
&#96;setfsuid&#96; and &#96;setfsgid&#96;. (These functions are
preferred over &#96;seteuid&#96; and &#96;setegid&#96; because they do
not allow the impersonated user to send signals to the process.) These
functions are not thread safe. In multi-threaded processes, these
operations need to be performed in a single-threaded child process.
Unexpected blocking may occur as well.

It is not recommended to try to reimplement the kernel permission checks
in user space because the required checks are complex. It is also very
difficult to avoid race conditions during path name resolution.

## File System Limits {#sect-Defensive_Coding-Tasks-File_System-Limits}

For historical reasons, there are preprocessor constants such as
&#96;PATH_MAX&#96;, &#96;NAME_MAX&#96;. However, on most systems, the
length of canonical path names (absolute path names with all symbolic
links resolved, as returned by &#96;realpath&#96; or
&#96;canonicalize_file_name&#96;) can exceed &#96;PATH_MAX&#96; bytes,
and individual file name components can be longer than
&#96;NAME_MAX&#96;. This is also true of the &#96;\_PC_PATH_MAX&#96; and
&#96;\_PC_NAME_MAX&#96; values returned by &#96;pathconf&#96;, and the
&#96;f_namemax&#96; member of &#96;struct statvfs&#96;. Therefore, these
constants should not be used. This is also reason why the
&#96;readdir_r&#96; should never be used (instead, use
&#96;readdir&#96;).

You should not write code in a way that assumes that there is an upper
limit on the number of subdirectories of a directory, the number of
regular files in a directory, or the link count of an inode.

## File system features {#sect-Defensive_Coding-Tasks-File_System-Features}

Not all file systems support all features. This makes it very difficult
to write general-purpose tools for copying files. For example, a copy
operation intending to preserve file permissions will generally fail
when copying to a FAT file system.

&#42; Some file systems are case-insensitive. Most should be
case-preserving, though.

&#42; Name length limits vary greatly, from eight to thousands of bytes.
Path length limits differ as well. Most systems impose an upper bound on
path names passed to the kernel, but using relative path names, it is
possible to create and access files whose absolute path name is
essentially of unbounded length.

&#42; Some file systems do not store names as fairly unrestricted byte
sequences, as it has been traditionally the case on GNU systems. This
means that some byte sequences (outside the POSIX safe character set)
are not valid names. Conversely, names of existing files may not be
representable as byte sequences, and the files are thus inaccessible on
GNU systems. Some file systems perform Unicode canonicalization on file
names. These file systems preserve case, but reading the name of a
just-created file using &#96;readdir&#96; might still result in a
different byte sequence.

&#42; Permissions and owners are not universally supported (and
SUID/SGID bits may not be available). For example, FAT file systems
assign ownership based on a mount option, and generally mark all files
as executable. Any attempt to change permissions would result in an
error.

&#42; Non-regular files (device nodes, FIFOs) are not generally
available.

&#42; Only on some file systems, files can have holes, that is, not all
of their contents is backed by disk storage.

&#42; &#96;ioctl&#96; support (even fairly generic functionality such as
&#96;FIEMAP&#96; for discovering physical file layout and holes) is
file-system-specific.

&#42; Not all file systems support extended attributes, ACLs and SELinux
metadata. Size and naming restriction on extended attributes vary.

&#42; Hard links may not be supported at all (FAT) or only within the
same directory (AFS). Symbolic links may not be available, either.
Reflinks (hard links with copy-on-write semantics) are still very rare.
Recent systems restrict creation of hard links to users which own the
target file or have read/write access to it, but older systems do not.

&#42; Renaming (or moving) files using &#96;rename&#96; can fail (even
when &#96;stat&#96; indicates that the source and target directories are
located on the same file system). This system call should work if the
old and new paths are located in the same directory, though.

&#42; Locking semantics vary among file systems. This affects advisory
and mandatory locks. For example, some network file systems do not allow
deleting files which are opened by any process.

&#42; Resolution of time stamps varies from two seconds to nanoseconds.
Not all time stamps are available on all file systems. File creation
time (&#42;birth time&#42;) is not exposed over the
&#96;stat&#96;/&#96;fstat&#96; interface, even if stored by the file
system.

## Checking Free Space {#sect-Defensive_Coding-Tasks-File_System-Free_Space}

The &#96;statvfs&#96; and &#96;fstatvfs&#96; functions allow programs to
examine the number of available blocks and inodes, through the members
&#96;f_bfree&#96;, &#96;f_bavail&#96;, &#96;f_ffree&#96;, and
&#96;f_favail&#96; of &#96;struct statvfs&#96;. Some file systems return
fictional values in the &#96;f_ffree&#96; and &#96;f_favail&#96; fields,
so the only reliable way to discover if the file system still has space
for a file is to try to create it. The &#96;f_bfree&#96; field should be
reasonably accurate, though.

# Temporary Files {#_temporary_files}

In this chapter, we describe how to create temporary files and
directories, how to remove them, and how to work with programs which do
not create files in ways that are safe with a shared directory for
temporary files. General file system manipulation is treated in a
separate chapter, [File System
Manipulation](tasks/Tasks-File_System.adoc&#35;chap-Defensive_Coding-Tasks-File_System).

Secure creation of temporary files has four different aspects.

&#42; The location of the directory for temporary files must be obtained
in a secure manner (that is, untrusted environment variables must be
ignored, see
xref:tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-secure_getenv\[Accessing
Environment Variables).

&#42; A new file must be created. Reusing an existing file must be
avoided (the &#96;/tmp&#96; race condition). This is tricky because
traditionally, system-wide temporary directories shared by all users are
used.

&#42; The file must be created in a way that makes it impossible for
other users to open it.

&#42; The descriptor for the temporary file should not leak to
subprocesses.

All functions mentioned below will take care of these aspects.

Traditionally, temporary files are often used to reduce memory usage of
programs. More and more systems use RAM-based file systems such as
&#96;tmpfs&#96; for storing temporary files, to increase performance and
decrease wear on Flash storage. As a result, spooling data to temporary
files does not result in any memory savings, and the related complexity
can be avoided if the data is kept in process memory.

## Obtaining the Location of Temporary Directory {#chap-Defensive_Coding-Tasks-Temporary_Files-Location}

Some functions below need the location of a directory which stores
temporary files. For C/C++ programs, use the following steps to obtain
that directory:

&#42; Use &#96;secure_getenv&#96; to obtain the value of the
&#96;TMPDIR&#96; environment variable. If it is set, convert the path to
a fully-resolved absolute path, using &#96;realpath(path, NULL)&#96;.
Check if the new path refers to a directory and is writeable. In this
case, use it as the temporary directory.

&#42; Fall back to &#96;/tmp&#96;.

In Python, you can use the &#96;tempfile.tempdir&#96; variable.

Java does not support SUID/SGID programs, so you can use the
&#96;java.lang.System.getenv(String)&#96; method to obtain the value of
the &#96;TMPDIR&#96; environment variable, and follow the two steps
described above. (Java's default directory selection does not honor
&#96;TMPDIR&#96;.)

## Named Temporary Files {#_named_temporary_files}

The &#96;mkostemp&#96; function creates a named temporary file. You
should specify the &#96;O_CLOEXEC&#96; flag to avoid file descriptor
leaks to subprocesses. (Applications which do not use multiple threads
can also use &#96;mkstemp&#96;, but libraries should use
&#96;mkostemp&#96;.) For determining the directory part of the file name
pattern, see
&lt;&lt;chap-Defensive_Coding-Tasks-Temporary_Files-Location&gt;&gt;

The file is not removed automatically. It is not safe to rename or
delete the file before processing, or transform the name in any way (for
example, by adding a file extension). If you need multiple temporary
files, call &#96;mkostemp&#96; multiple times. Do not create additional
file names derived from the name provided by a previous
&#96;mkostemp&#96; call. However, it is safe to close the descriptor
returned by &#96;mkostemp&#96; and reopen the file using the generated
name.

The Python class &#96;tempfile.NamedTemporaryFile&#96; provides similar
functionality, except that the file is deleted automatically by default.
Note that you may have to use the &#96;file&#96; attribute to obtain the
actual file object because some programming interfaces cannot deal with
file-like objects. The C function &#96;mkostemp&#96; is also available
as &#96;tempfile.mkstemp&#96;.

In Java, you can use the &#96;java.io.File.createTempFile(String,
String, File)&#96; function, using the temporary file location
determined according to
&lt;&lt;chap-Defensive_Coding-Tasks-Temporary_Files-Location&gt;&gt;. Do
not use &#96;java.io.File.deleteOnExit()&#96; to delete temporary files,
and do not register a shutdown hook for each temporary file you create.
In both cases, the deletion hint cannot be removed from the system if
you delete the temporary file prior to termination of the VM, causing a
memory leak.

## Temporary Files without Names {#_temporary_files_without_names}

The &#96;tmpfile&#96; function creates a temporary file and immediately
deletes it, while keeping the file open. As a result, the file lacks a
name and its space is deallocated as soon as the file descriptor is
closed (including the implicit close when the process terminates). This
avoids cluttering the temporary directory with orphaned files.

Alternatively, if the maximum size of the temporary file is known
beforehand, the &#96;fmemopen&#96; function can be used to create a
&#96;FILE &#42;&#96; object which is backed by memory.

In Python, unnamed temporary files are provided by the
&#96;tempfile.TemporaryFile&#96; class, and the
&#96;tempfile.SpooledTemporaryFile&#96; class provides a way to avoid
creation of small temporary files.

Java does not support unnamed temporary files.

## Temporary Directories {#chap-Defensive_Coding-Tasks-Temporary_Directory}

The &#96;mkdtemp&#96; function can be used to create a temporary
directory. (For determining the directory part of the file name pattern,
see
&lt;&lt;chap-Defensive_Coding-Tasks-Temporary_Files-Location&gt;&gt;.)
The directory is not automatically removed. In Python, this function is
available as &#96;tempfile.mkdtemp&#96;. In Java 7, temporary
directories can be created using the
&#96;java.nio.file.Files.createTempDirectory(Path, String,
FileAttribute&#8230;)&#96; function.

When creating files in the temporary directory, use automatically
generated names, e.g., derived from a sequential counter. Files with
externally provided names could be picked up in unexpected contexts, and
crafted names could actually point outside of the tempoary directory
(due to &#42;directory traversal&#42;).

Removing a directory tree in a completely safe manner is complicated.
Unless there are overriding performance concerns, the
\[application\]&#42;rm&#42; program should be used, with the
\[option\]&#96;-rf&#96; and \[option\]&#96;\--&#96; options.

## Compensating for Unsafe File Creation {#_compensating_for_unsafe_file_creation}

There are two ways to make a function or program which excepts a file
name safe for use with temporary files. See [Creating Safe
Processes](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-Processes-Creation)
for details on subprocess creation.

&#42; Create a temporary directory and place the file there. If
possible, run the program in a subprocess which uses the temporary
directory as its current directory, with a restricted environment. Use
generated names for all files in that temporary directory. (See
&lt;&lt;chap-Defensive_Coding-Tasks-Temporary_Directory&gt;&gt;.)

&#42; Create the temporary file and pass the generated file name to the
function or program. This only works if the function or program can cope
with a zero-length existing file. It is safe only under additional
assumptions:

\+ &#42;&#42; The function or program must not create additional files
whose name is derived from the specified file name or are otherwise
predictable.

\+ &#42;&#42; The function or program must not delete the file before
processing it.

\+ &#42;&#42; It must not access any existing files in the same
directory.

\+ It is often difficult to check whether these additional assumptions
are matched, therefore this approach is not recommended.

# Processes {#_processes}

## Creating Safe Processes {#sect-Defensive_Coding-Tasks-Processes-Creation}

This section describes how to create new child processes in a safe
manner. In addition to the concerns addressed below, there is the
possibility of file descriptor leaks, see [Preventing File Descriptor
Leaks to Child
Processes](tasks/Tasks-Descriptors.adoc&#35;sect-Defensive_Coding-Tasks-Descriptors-Child_Processes).

### Obtaining the Program Path and the Command-line Template {#_obtaining_the_program_path_and_the_command_line_template}

The name and path to the program being invoked should be hard-coded or
controlled by a static configuration file stored at a fixed location (at
an file system absolute path). The same applies to the template for
generating the command line.

The configured program name should be an absolute path. If it is a
relative path, the contents of the &#96;PATH&#96; must be obtained in a
secure manner (see
&lt;&lt;sect-Defensive_Coding-Tasks-secure_getenv&gt;&gt;). If the
&#96;PATH&#96; variable is not set or untrusted, the safe default
&#96;/bin:/usr/bin&#96; must be used.

If too much flexibility is provided here, it may allow invocation of
arbitrary programs without proper authorization.

### Bypassing the Shell {#sect-Defensive_Coding-Tasks-Processes-execve}

Child processes should be created without involving the system shell.

For C/C++, &#96;system&#96; should not be used. The
&#96;posix_spawn&#96; function can be used instead, or a combination
&#96;fork&#96; and &#96;execve&#96;. (In some cases, it may be
preferable to use &#96;vfork&#96; or the Linux-specific &#96;clone&#96;
system call instead of &#96;fork&#96;.)

In Python, the &#96;subprocess&#96; module bypasses the shell by default
(when the &#96;shell&#96; keyword argument is not set to true).
&#96;os.system&#96; should not be used.

The Java class &#96;java.lang.ProcessBuilder&#96; can be used to create
subprocesses without interference from the system shell.

:::: important
::: title
Portability notice
:::

On Windows, there is no argument vector, only a single argument string.
Each application is responsible for parsing this string into an argument
vector. There is considerable variance among the quoting style
recognized by applications. Some of them expand shell wildcards, others
do not. Extensive application-specific testing is required to make this
secure.
::::

Note that some common applications (notably
\[application\]&#42;ssh&#42;) unconditionally introduce the use of a
shell, even if invoked directly without a shell. It is difficult to use
these applications in a secure manner. In this case, untrusted data
should be supplied by other means. For example, standard input could be
used, instead of the command line.

### Specifying the Process Environment {#sect-Defensive_Coding-Tasks-Processes-environ}

Child processes should be created with a minimal set of environment
variables. This is absolutely essential if there is a trust transition
involved, either when the parent process was created, or during the
creation of the child process.

In C/C++, the environment should be constructed as an array of strings
and passed as the &#96;envp&#96; argument to &#96;posix_spawn&#96; or
&#96;execve&#96;. The functions &#96;setenv&#96;, &#96;unsetenv&#96; and
&#96;putenv&#96; should not be used. They are not thread-safe and suffer
from memory leaks.

Python programs need to specify a &#96;dict&#96; for the the
&#96;env&#96; argument of the &#96;subprocess.Popen&#96; constructor.
The Java class &#96;java.lang.ProcessBuilder&#96; provides a
&#96;environment()&#96; method, which returns a map that can be
manipulated.

The following list provides guidelines for selecting the set of
environment variables passed to the child process.

&#42; &#96;PATH&#96; should be initialized to &#96;/bin:/usr/bin&#96;.

&#42; &#96;USER&#96; and &#96;HOME&#96; can be inhereted from the parent
process environment, or they can be initialized from the &#96;pwent&#96;
structure for the user.

&#42; The &#96;DISPLAY&#96; and &#96;XAUTHORITY&#96; variables should be
passed to the subprocess if it is an X program. Note that this will
typically not work across trust boundaries because &#96;XAUTHORITY&#96;
refers to a file with &#96;0600&#96; permissions.

&#42; The location-related environment variables &#96;LANG&#96;,
&#96;LANGUAGE&#96;, &#96;LC_ADDRESS&#96;, &#96;LC_ALL&#96;,
&#96;LC_COLLATE&#96;, &#96;LC_CTYPE&#96;, &#96;LC_IDENTIFICATION&#96;,
&#96;LC_MEASUREMENT&#96;, &#96;LC_MESSAGES&#96;, &#96;LC_MONETARY&#96;,
&#96;LC_NAME&#96;, &#96;LC_NUMERIC&#96;, &#96;LC_PAPER&#96;,
&#96;LC_TELEPHONE&#96; and &#96;LC_TIME&#96; can be passed to the
subprocess if present.

&#42; The called process may need application-specific environment
variables, for example for passing passwords. (See
&lt;&lt;sect-Defensive_Coding-Tasks-Processes-Command_Line_Visibility&gt;&gt;.)

&#42; All other environment variables should be dropped. Names for new
environment variables should not be accepted from untrusted sources.

### Robust Argument List Processing {#_robust_argument_list_processing}

When invoking a program, it is sometimes necessary to include data from
untrusted sources. Such data should be checked against embedded
&#96;NUL&#96; characters because the system APIs will silently truncate
argument strings at the first &#96;NUL&#96; character.

The following recommendations assume that the program being invoked uses
GNU-style option processing using &#96;getopt_long&#96;. This convention
is widely used, but it is just that, and individual programs might
interpret a command line in a different way.

If the untrusted data has to go into an option, use the
&#96;\--option-name=VALUE&#96; syntax, placing the option and its value
into the same command line argument. This avoids any potential confusion
if the data starts with &#96;-&#96;.

For positional arguments, terminate the option list with a single
\[option\]&#96;\--&#96; marker after the last option, and include the
data at the right position. The \[option\]&#96;\--&#96; marker
terminates option processing, and the data will not be treated as an
option even if it starts with a dash.

### Passing Secrets to Subprocesses {#sect-Defensive_Coding-Tasks-Processes-Command_Line_Visibility}

The command line (the name of the program and its argument) of a running
process is traditionally available to all local users. The called
program can overwrite this information, but only after it has run for a
bit of time, during which the information may have been read by other
processes. However, on Linux, the process environment is restricted to
the user who runs the process. Therefore, if you need a convenient way
to pass a password to a child process, use an environment variable, and
not a command line argument. (See
&lt;&lt;sect-Defensive_Coding-Tasks-Processes-environ&gt;&gt;.)

:::: important
::: title
Portability notice
:::

On some UNIX-like systems (notably Solaris), environment variables can
be read by any system user, just like command lines.
::::

If the environment-based approach cannot be used due to portability
concerns, the data can be passed on standard input. Some programs
(notably \[application\]&#42;gpg&#42;) use special file descriptors
whose numbers are specified on the command line. Temporary files are an
option as well, but they might give digital forensics access to
sensitive data (such as passphrases) because it is difficult to safely
delete them in all cases.

## Handling Child Process Termination {#_handling_child_process_termination}

When child processes terminate, the parent process is signalled. A stub
of the terminated processes (a &#42;zombie&#42;, shown as
&#96;&lt;defunct&gt;&#96; by \[application\]&#42;ps&#42;) is kept around
until the status information is collected (&#42;reaped&#42;) by the
parent process. Over the years, several interfaces for this have been
invented:

&#42; The parent process calls &#96;wait&#96;, &#96;waitpid&#96;,
&#96;waitid&#96;, &#96;wait3&#96; or &#96;wait4&#96;, without specifying
a process ID. This will deliver any matching process ID. This approach
is typically used from within event loops.

&#42; The parent process calls &#96;waitpid&#96;, &#96;waitid&#96;, or
&#96;wait4&#96;, with a specific process ID. Only data for the specific
process ID is returned. This is typically used in code which spawns a
single subprocess in a synchronous manner.

&#42; The parent process installs a handler for the &#96;SIGCHLD&#96;
signal, using &#96;sigaction&#96;, and specifies to the
&#96;SA_NOCLDWAIT&#96; flag. This approach could be used by event loops
as well.

None of these approaches can be used to wait for child process
terminated in a completely thread-safe manner. The parent process might
execute an event loop in another thread, which could pick up the
termination signal. This means that libraries typically cannot make free
use of child processes (for example, to run problematic code with
reduced privileges in a separate address space).

At the moment, the parent process should explicitly wait for termination
of the child process using &#96;waitpid&#96; or &#96;waitid&#96;, and
hope that the status is not collected by an event loop first.

## &#96;SUID&#96;/&#96;SGID&#96; processes {#_96suid9696sgid96_processes}

Programs can be marked in the file system to indicate to the kernel that
a trust transition should happen if the program is run. The
&#96;SUID&#96; file permission bit indicates that an executable should
run with the effective user ID equal to the owner of the executable
file. Similarly, with the &#96;SGID&#96; bit, the effective group ID is
set to the group of the executable file.

Linux supports &#42;fscaps&#42;, which can grant additional capabilities
to a process in a finer-grained manner. Additional mechanisms can be
provided by loadable security modules.

When such a trust transition has happened, the process runs in a
potentially hostile environment. Additional care is necessary not to
rely on any untrusted information. These concerns also apply to
libraries which can be linked into such processes.

### Accessing Environment Variables {#sect-Defensive_Coding-Tasks-secure_getenv}

The following steps are required so that a program does not accidentally
pick up untrusted data from environment variables.

&#42; Compile your C/C++ sources with &#96;-D_GNU_SOURCE&#96;. The
Autoconf macro &#96;AC_GNU_SOURCE&#96; ensures this.

&#42; Check for the presence of the &#96;secure_getenv&#96; and
&#96;+*secure_getenv+&#96; function. The Autoconf directive
&#96;+AC_CHECK_FUNCS(\[*secure_getenv secure_getenv\])+&#96; performs
these checks.

&#42; Arrange for a proper definition of the &#96;secure_getenv&#96;
function. See &lt;&lt;ex-Defensive_Coding-Tasks-secure_getenv&gt;&gt;.

&#42; Use &#96;secure_getenv&#96; instead of &#96;getenv&#96; to obtain
the value of critical environment variables. &#96;secure_getenv&#96;
will pretend the variable has not bee set if the process environment is
not trusted.

Critical environment variables are debugging flags, configuration file
locations, plug-in and log file locations, and anything else that might
be used to bypass security restrictions or cause a privileged process to
behave in an unexpected way.

Either the &#96;secure_getenv&#96; function or the
&#96;+\_\_secure_getenv+&#96; is available from GNU libc.

:::: {#ex-Defensive_Coding-Tasks-secure_getenv .example}
::: title
Obtaining a definition for &#96;secure_getenv&#96;
:::

``` c
\&#35;include \&lt;stdlib.h\&gt;

\&#35;ifndef HAVE_SECURE_GETENV
\&#35;  ifdef HAVE__SECURE_GETENV
\&#35;    define secure_getenv __secure_getenv
\&#35;  else
\&#35;    error neither secure_getenv nor __secure_getenv are available
\&#35;  endif
\&#35;endif
```
::::

## Daemons {#sect-Defensive_Coding-Tasks-Processes-Daemons}

Background processes providing system services (&#42;daemons&#42;) need
to decouple themselves from the controlling terminal and the parent
process environment:

&#42; Fork.

&#42; In the child process, call &#96;setsid&#96;. The parent process
can simply exit (using &#96;\_exit&#96;, to avoid running clean-up
actions twice).

&#42; In the child process, fork again. Processing continues in the
child process. Again, the parent process should just exit.

&#42; Replace the descriptors 0, 1, 2 with a descriptor for
&#96;/dev/null&#96;. Logging should be redirected to
\[application\]&#42;syslog&#42;.

Older instructions for creating daemon processes recommended a call to
&#96;umask(0)&#96;. This is risky because it often leads to
world-writable files and directories, resulting in security
vulnerabilities such as arbitrary process termination by untrusted local
users, or log file truncation. If the &#42;umask&#42; needs setting, a
restrictive value such as &#96;027&#96; or &#96;077&#96; is recommended.

Other aspects of the process environment may have to changed as well
(environment variables, signal handler disposition).

It is increasingly common that server processes do not run as background
processes, but as regular foreground process under a supervising master
process (such as \[application\]&#42;systemd&#42;). Server processes
should offer a command line option which disables forking and
replacement of the standard output and standard error streams. Such an
option is also useful for debugging.

## Semantics of Command-line Arguments {#_semantics_of_command_line_arguments}

After process creation and option processing, it is up to the child
process to interpret the arguments. Arguments can be file names, host
names, or URLs, and many other things. URLs can refer to the local
network, some server on the Internet, or to the local file system. Some
applications even accept arbitrary code in arguments (for example,
\[application\]&#42;python&#42; with the \[option\]&#96;-c&#96; option).

Similar concerns apply to environment variables, the contents of the
current directory and its subdirectories.

Consequently, careful analysis is required if it is safe to pass
untrusted data to another program.

## &#96;fork&#96; as a Primitive for Parallelism {#sect-Defensive_Coding-Tasks-Processes-Fork-Parallel}

A call to &#96;fork&#96; which is not immediately followed by a call to
&#96;execve&#96; (perhaps after rearranging and closing file
descriptors) is typically unsafe, especially from a library which does
not control the state of the entire process. Such use of &#96;fork&#96;
should be replaced with proper child processes or threads.

# Serialization and Deserialization {#_serialization_and_deserialization}

Protocol decoders and file format parsers are often the most-exposed
part of an application because they are exposed with little or no user
interaction and before any authentication and security checks are made.
They are also difficult to write robustly in languages which are not
memory-safe.

## Recommendations for Manually-written Decoders {#sect-Defensive_Coding-Tasks-Serialization-Decoders}

For C and C++, the advice in [Recommendations for Pointers and Array
Handling](programming-languages/C.adoc&#35;sect-Defensive_Coding-C-Pointers)
applies. In addition, avoid non-character pointers directly into input
buffers. Pointer misalignment causes crashes on some architectures.

When reading variable-sized objects, do not allocate large amounts of
data solely based on the value of a size field. If possible, grow the
data structure as more data is read from the source, and stop when no
data is available. This helps to avoid denial-of-service attacks where
little amounts of input data results in enormous memory allocations
during decoding. Alternatively, you can impose reasonable bounds on
memory allocations, but some protocols do not permit this.

## Protocol Design {#_protocol_design}

Binary formats with explicit length fields are more difficult to parse
robustly than those where the length of dynamically-sized elements is
derived from sentinel values. A protocol which does not use length
fields and can be written in printable ASCII characters simplifies
testing and debugging. However, binary protocols with length fields may
be more efficient to parse.

In new datagram-oriented protocols, unique numbers such as sequence
numbers or identifiers for fragment reassembly (see
&lt;&lt;sect-Defensive_Coding-Tasks-Serialization-Fragmentation&gt;&gt;)
should be at least 64 bits large, and really should not be smaller than
32 bits in size. Protocols should not permit fragments with overlapping
contents.

## Fragmentation {#sect-Defensive_Coding-Tasks-Serialization-Fragmentation}

Some serialization formats use frames or protocol data units (PDUs) on
lower levels which are smaller than the PDUs on higher levels. With such
an architecture, higher-level PDUs may have to be &#42;fragmented&#42;
into smaller frames during serialization, and frames may need
&#42;reassembly&#42; into large PDUs during deserialization.

Serialization formats may use conceptually similar structures for
completely different purposes, for example storing multiple layers and
color channels in a single image file.

When fragmenting PDUs, establish a reasonable lower bound for the size
of individual fragments (as large as possible---limits as low as one or
even zero can add substantial overhead). Avoid fragmentation if at all
possible, and try to obtain the maximum acceptable fragment length from
a trusted data source.

When implementing reassembly, consider the following aspects.

&#42; Avoid allocating significant amount of resources without proper
authentication. Allocate memory for the unfragmented PDU as more and
more and fragments are encountered, and not based on the initially
advertised unfragmented PDU size, unless there is a sufficiently low
limit on the unfragmented PDU size, so that over-allocation cannot lead
to performance problems.

&#42; Reassembly queues on top of datagram-oriented transports should be
bounded, both in the combined size of the arrived partial PDUs waiting
for reassembly, and the total number of partially reassembled fragments.
The latter limit helps to reduce the risk of accidental reassembly of
unrelated fragments, as it can happen with small fragment IDs (see
&lt;&lt;sect-Defensive_Coding-Tasks-Serialization-Fragmentation-ID&gt;&gt;).
It also guards to some extent against deliberate injection of fragments,
by guessing fragment IDs.

&#42; Carefully keep track of which bytes in the unfragmented PDU have
been covered by fragments so far. If message reordering is a concern,
the most straightforward data structure for this is an array of bits,
with one bit for every byte (or other atomic unit) in the unfragmented
PDU. Complete reassembly can be determined by increasing a counter of
set bits in the bit array as the bit array is updated, taking
overlapping fragments into consideration.

&#42; Reject overlapping fragments (that is, multiple fragments which
provide data at the same offset of the PDU being fragmented), unless the
protocol explicitly requires accepting overlapping fragments. The bit
array used for tracking already arrived bytes can be used for this
purpose.

&#42; Check for conflicting values of unfragmented PDU lengths (if this
length information is part of every fragment) and reject fragments which
are inconsistent.

&#42; Validate fragment lengths and offsets of individual fragments
against the unfragmented PDU length (if they are present). Check that
the last byte in the fragment does not lie after the end of the
unfragmented PDU. Avoid integer overflows in these computations (see
[Recommendations for Integer
Arithmetic](programming-languages/C.adoc&#35;sect-Defensive_Coding-C-Arithmetic)).

### Fragment IDs {#sect-Defensive_Coding-Tasks-Serialization-Fragmentation-ID}

If the underlying transport is datagram-oriented (so that PDUs can be
reordered, duplicated or be lost, like with UDP), fragment reassembly
needs to take into account endpoint addresses of the communication
channel, and there has to be some sort of fragment ID which identifies
the individual fragments as part of a larger PDU. In addition, the
fragmentation protocol will typically involve fragment offsets and
fragment lengths, as mentioned above.

If the transport may be subject to blind PDU injection (again, like
UDP), the fragment ID must be generated randomly. If the fragment ID is
64 bit or larger (strongly recommended), it can be generated in a
completely random fashion for most traffic volumes. If it is less than
64 bits large (so that accidental collisions can happen if a lot of PDUs
are transmitted), the fragment ID should be incremented sequentially
from a starting value. The starting value should be derived using a
HMAC-like construction from the endpoint addresses, using a long-lived
random key. This construction ensures that despite the limited range of
the ID, accidental collisions are as unlikely as possible. (This will
not work reliable with really short fragment IDs, such as the 16 bit IDs
used by the Internet Protocol.)

## Library Support for Deserialization {#sect-Defensive_Coding-Tasks-Serialization-Library}

There are too many subtleties when dealing with Deserialization to be
discussed here. A more detailed and updated guide is available as [OWASP
Deserialization Cheat
Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html).

## XML Serialization {#sect-Defensive_Coding-Tasks-Serialization-XML}

### External References {#sect-Defensive_Coding-Tasks-Serialization-XML-External}

XML documents can contain external references. They can occur in various
places.

&#42; In the DTD declaration in the header of an XML document:

\+

``` xml
\&lt;!DOCTYPE html PUBLIC
'-//W3C//DTD XHTML 1.0 Transitional//EN'
'http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd'\&gt;
```

&#42; In a namespace declaration:

\+

``` xml
\&lt;xsd:schema xmlns:xsd='http://www.w3.org/2001/XMLSchema'\&gt;
```

&#42; In an entity definition:

\+

``` xml
\&lt;!ENTITY sys SYSTEM 'http://www.example.com/ent.adoc[]\&gt;
\&lt;!ENTITY pub PUBLIC '-//Example//Public Entity//EN'
'http://www.example.com/pub-ent.adoc[]\&gt;
```

&#42; In a notation:

\+

``` xml
\&lt;!NOTATION not SYSTEM '../not.adoc[]\&gt;
```

Originally, these external references were intended as unique
identifiers, but by many XML implementations, they are used for locating
the data for the referenced element. This causes unwanted network
traffic, and may disclose file system contents or otherwise unreachable
network resources, so this functionality should be disabled.

Depending on the XML library, external referenced might be processed not
just when parsing XML, but also when generating it.

### Entity Expansion {#sect-Defensive_Coding-Tasks-Serialization-XML-Entities}

When external DTD processing is disabled, an internal DTD subset can
still contain entity definitions. Entity declarations can reference
other entities. Some XML libraries expand entities automatically, and
this processing cannot be switched off in some places (such as attribute
values or content models). Without limits on the entity nesting level,
this expansion results in data which can grow exponentially in length
with size of the input. (If there is a limit on the nesting level, the
growth is still polynomial, unless further limits are imposed.)

Consequently, the processing internal DTD subsets should be disabled if
possible, and only trusted DTDs should be processed. If a particular XML
application does not permit such restrictions, then application-specific
limits are called for.

### XInclude Processing {#sect-Defensive_Coding-Tasks-Serialization-XML-XInclude}

XInclude processing can reference file and network resources and include
them into the document, much like external entity references. When
parsing untrusted XML documents, XInclude processing should be turned
off.

XInclude processing is also fairly complex and may pull in support for
the XPointer and XPath specifications, considerably increasing the
amount of code required for XML processing.

### Algorithmic Complexity of XML Validation {#sect-Defensive_Coding-Tasks-Serialization-XML-Validation}

DTD-based XML validation uses regular expressions for content models.
The XML specification requires that content models are deterministic,
which means that efficient validation is possible. However, some
implementations do not enforce determinism, and require exponential (or
just polynomial) amount of space or time for validating some
DTD/document combinations.

XML schemas and RELAX NG (via the &#96;xsd:&#96; prefix) directly
support textual regular expressions which are not required to be
deterministic.

### Using Expat for XML parsing {#sect-Defensive_Coding-Tasks-Serialization-XML-Expat}

By default, Expat does not try to resolve external IDs, so no steps are
required to block them. However, internal entity declarations are
processed. Installing a callback which stops parsing as soon as such
entities are encountered disables them, see
&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-Expat-EntityDeclHandler&gt;&gt;.
Expat does not perform any validation, so there are no problems related
to that.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-Expat-EntityDeclHandler .example}
::: title
Disabling XML entity processing with Expat
:::

``` java
```
::::

This handler must be installed when the &#96;XML_Parser&#96; object is
created
(&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-Expat-Create&gt;&gt;).

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-Expat-Create .example}
::: title
Creating an Expat XML parser
:::

``` java
```
::::

It is also possible to reject internal DTD subsets altogether, using a
suitable &#96;XML_StartDoctypeDeclHandler&#96; handler installed with
&#96;XML_SetDoctypeDeclHandler&#96;.

### Using Qt for XML Parsing {#sect-Defensive_Coding-Tasks-Serialization-Qt}

The XML component of Qt, QtXml, does not resolve external IDs by
default, so it is not required to prevent such resolution. Internal
entities are processed, though. To change that, a custom
&#96;QXmlDeclHandler&#96; and &#96;QXmlSimpleReader&#96; subclasses are
needed. It is not possible to use the
&#96;QDomDocument::setContent(const QByteArray &amp;)&#96; convenience
methods.

&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-Qt-NoEntityHandler&gt;&gt;
shows an entity handler which always returns errors, causing parsing to
stop when encountering entity declarations.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-Qt-NoEntityHandler .example}
::: title
A QtXml entity handler which blocks entity processing
:::

``` java
```
::::

This handler is used in the custom &#96;QXmlReader&#96; subclass in
&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-Qt-NoEntityReader&gt;&gt;.
Some parts of QtXml will call the &#96;setDeclHandler(QXmlDeclHandler
&#42;)&#96; method. Consequently, we prevent overriding our custom
handler by providing a definition of this method which does nothing. In
the constructor, we activate namespace processing; this part may need
adjusting.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-Qt-NoEntityReader .example}
::: title
A QtXml XML reader which blocks entity processing
:::

``` java
```
::::

Our &#96;NoEntityReader&#96; class can be used with one of the
overloaded &#96;QDomDocument::setContent&#96; methods.
&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-Qt-QDomDocument&gt;&gt;
shows how the &#96;buffer&#96; object (of type &#96;QByteArray&#96;) is
wrapped as a &#96;QXmlInputSource&#96;. After calling the
&#96;setContent&#96; method, you should check the return value and
report any error.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-Qt-QDomDocument .example}
::: title
Parsing an XML document with QDomDocument, without entity expansion
:::

``` java
```
::::

### Using OpenJDK for XML Parsing and Validation {#sect-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse}

OpenJDK contains facilities for DOM-based, SAX-based, and StAX-based
document parsing. Documents can be validated against DTDs or XML
schemas.

The approach taken to deal with entity expansion differs from the
general recommendation in
&lt;&lt;sect-Defensive_Coding-Tasks-Serialization-XML-Entities&gt;&gt;.
We enable the the feature flag
&#96;javax.xml.XMLConstants.FEATURE_SECURE_PROCESSING&#96;, which
enforces heuristic restrictions on the number of entity expansions. Note
that this flag alone does not prevent resolution of external references
(system IDs or public IDs), so it is slightly misnamed.

In the following sections, we use helper classes to prevent external ID
resolution.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK-NoEntityResolver .example}
::: title
Helper class to prevent DTD external entity resolution in OpenJDK
:::

``` java
```
::::

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK-NoResourceResolver .example}
::: title
Helper class to prevent schema resolution in OpenJDK
:::

``` java
```
::::

&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK-Imports&gt;&gt;
shows the imports used by the examples.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK-Imports .example}
::: title
Java imports for OpenJDK XML parsing
:::

``` java
```
::::

#### DOM-based XML parsing and DTD validation in OpenJDK {#sect-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-DOM}

This approach produces a &#96;org.w3c.dom.Document&#96; object from an
input stream.
&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-DOM&gt;&gt;
use the data from the &#96;java.io.InputStream&#96; instance in the
&#96;inputStream&#96; variable.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-DOM .example}
::: title
DOM-based XML parsing in OpenJDK
:::

``` java
```
::::

External entity references are prohibited using the
&#96;NoEntityResolver&#96; class in
&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK-NoEntityResolver&gt;&gt;.
Because external DTD references are prohibited, DTD validation (if
enabled) will only happen against the internal DTD subset embedded in
the XML document.

To validate the document against an external DTD, use a
&#96;javax.xml.transform.Transformer&#96; class to add the DTD reference
to the document, and an entity resolver which whitelists this external
reference.

#### XML Schema Validation in OpenJDK {#sect-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-SAX}

&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-XMLSchema_SAX&gt;&gt;
shows how to validate a document against an XML Schema, using a
SAX-based approach. The XML data is read from an
&#96;java.io.InputStream&#96; in the &#96;inputStream&#96; variable.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-XMLSchema_SAX .example}
::: title
SAX-based validation against an XML schema in OpenJDK
:::

``` java
```
::::

The &#96;NoResourceResolver&#96; class is defined in
&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK-NoResourceResolver&gt;&gt;.

If you need to validate a document against an XML schema, use the code
in
&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-DOM&gt;&gt;
to create the document, but do not enable validation at this point. Then
use
&lt;&lt;ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-XMLSchema_DOM&gt;&gt;
to perform the schema-based validation on the
&#96;org.w3c.dom.Document&#96; instance &#96;document&#96;.

:::: {#ex-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-XMLSchema_DOM .example}
::: title
Validation of a DOM document against an XML schema in OpenJDK
:::

``` java
```
::::

#### Other XML Parsers in OpenJDK {#sect-Defensive_Coding-Tasks-Serialization-XML-OpenJDK_Parse-Other}

OpenJDK contains additional XML parsing and processing facilities. Some
of them are insecure.

The class &#96;java.beans.XMLDecoder&#96; acts as a bridge between the
Java object serialization format and XML. It is close to impossible to
securely deserialize Java objects in this format from untrusted inputs,
so its use is not recommended, as with the Java object serialization
format itself. See
&lt;&lt;sect-Defensive_Coding-Tasks-Serialization-Library&gt;&gt;.

## Protocol Encoders {#_protocol_encoders}

For protocol encoders, you should write bytes to a buffer which grows as
needed, using an exponential sizing policy. Explicit lengths can be
patched in later, once they are known. Allocating the required number of
bytes upfront typically requires separate code to compute the final
size, which must be kept in sync with the actual encoding step, or
vulnerabilities may result. In multi-threaded code, parts of the object
being deserialized might change, so that the computed size is out of
date.

You should avoid copying data directly from a received packet during
encoding, disregarding the format. Propagating malformed data could
enable attacks on other recipients of that data.

When using C or C++ and copying whole data structures directly into the
output, make sure that you do not leak information in padding bytes
between fields or at the end of the &#96;struct&#96;.

# Cryptography {#_cryptography}

## Primitives {#_primitives}

Choosing from the following cryptographic primitives is recommended:

&#42; RSA with 2048-bit keys and OAEP or PSS padding

&#42; AES-128 in CBC mode

&#42; AES-128 in GCM mode

&#42; AES-256 in CBC mode

&#42; AES-256 in GCM mode

&#42; SHA-256

&#42; HMAC-SHA-256

&#42; HMAC-SHA-1

Other cryptographic algorithms can be used if they are required for
interoperability with existing software:

&#42; RSA with key sizes larger than 1024 and legacy padding

&#42; AES-192

&#42; 3DES (triple DES, with two or three 56-bit keys), but strongly
discouraged

&#42; RC4 (but very, very strongly discouraged)

&#42; SHA-1

&#42; HMAC-MD5

:::: important
::: title
Important
:::

These primitives are difficult to use in a secure way. Custom
implementation of security protocols should be avoided. For protecting
confidentiality and integrity of network transmissions, TLS should be
used ([Transport Layer
Security](features/Features-TLS.adoc&#35;chap-Defensive_Coding-TLS)).

In particular, when using AES in CBC mode, it is necessary to add
integrity checking by other means, preferably using HMAC-SHA-256 and
&#42;after&#42; encryption (that is, on the encrypted cipher text). For
AES in GCM mode, correct construction of nonces is absolutely essential.
::::

## Randomness {#_randomness}

The following facilities can be used to generate unpredictable and
non-repeating values. When these functions are used without special
safeguards, each individual random value should be at least 12 bytes
long.

&#42; &#96;PK11_GenerateRandom&#96; in the NSS library (usable for high
data rates)

&#42; &#96;RAND_bytes&#96; in the OpenSSL library (usable for high data
rates)

&#42; &#96;gnutls_rnd&#96; in GNUTLS, with &#96;GNUTLS_RND_RANDOM&#96;
as the first argument (usable for high data rates)

&#42; &#96;java.security.SecureRandom&#96; in Java (usable for high data
rates)

&#42; The &#96;secrets&#96; module in Python. Older versions of Python
(pre 3.6) can use &#96;os.urandom&#96;

&#42; The &#96;getrandom&#96; system call since glibc 2.25

&#42; The &#96;getentropy&#96; call since glibc 2.25

&#42; Reading from the &#96;/dev/urandom&#96; character device

All these functions should be non-blocking, and they should not wait
until physical randomness becomes available. (Some cryptography
providers for Java can cause &#96;java.security.SecureRandom&#96; to
block, however.) Those functions which do not obtain all bits directly
from &#96;/dev/urandom&#96; are suitable for high data rates because
they do not deplete the system-wide entropy pool.

:::: important
::: title
Difficult to use API
:::

Both &#96;RAND_bytes&#96; and &#96;PK11_GenerateRandom&#96; have
three-state return values (with conflicting meanings). Careful error
checking is required. Please review the documentation when using these
functions.
::::

:::: important
::: title
Difficult to use API
:::

The &#96;getrandom&#96; system call has three-state return values, hence
requires careful error checking.

It was introduced in Linux kernel 3.17, but before glibc 2.25 no API
wrappers were provided. As such one could only use it via the syscall
interface as &#96;syscall(SYS_getrandom, (void&#42;)dest, (size_t)size,
(unsigned int)0)&#96;. For portable code targeting multiple kernel
versions one has to check for the function beingavailable on run-time,
and switch to another facility if the running kernel does not support
this call.
::::

Other sources of randomness should be considered predictable.

Generating randomness for cryptographic keys in long-term use may need
different steps and is best left to cryptographic libraries.

## Removing Sensitive information from memory {#_removing_sensitive_information_from_memory}

Sensitive data such as password, cryptographic keys etc, should be
removed from memory as soon as possible, once this information is no
longer required.

However compiler optimizations make this erasure operation difficult,
since the compiler deems this code as unnecessary and often removes it
from the compiled binary. For example a call to memset or a loop which
zero's out each byte of an array may be optimized out during
compilation.

This problem can be addressed by using &#96;explicit_bzero()&#96;. Calls
to this function are never optimized by the compiler.

However, as per the &#96;explicit_bzero()&#96; documentation there are
some things to consider:

&#42; The &#96;explicit_bzero()&#96; function does not guarantee that
sensitive data is completely erased from memory. For example, there may
be copies of the sensitive data in a register and in \'scratch\' stack
areas. The &#96;explicit_bzero()&#96; function is not aware of these
copies, and can't erase them.

&#42; In some circumstances, &#96;explicit_bzero()&#96; can decrease
security. If the compiler determined that the variable containing the
sensitive data could be optimized to be stored in a register (because it
is small enough to fit in a register, and no operation other than the
&#96;explicit_bzero()&#96; call would need to take the address of the
variable), then the &#96;explicit_bzero()&#96; call will force the data
to be copied from the register to a location in RAM that is then
immediately erased (while the copy in the register remains unaffected).
The problem here is that data in RAM is more likely to be exposed by a
bug than data in a register, and thus the &#96;explicit_bzero()&#96;
call creates a brief time window where the sensitive data is more
vulnerable than it would otherwise have been if no attempt had been made
to erase the data.

# RPM Packaging {#_rpm_packaging}

This chapter deals with security-related concerns around RPM packaging.
It has to be read in conjunction with distribution-specific packaging
guidelines.

## Generating X.509 Self-signed Certificates during Installation {#sect-Defensive_Coding-Tasks-Packaging-Certificates}

Some applications need X.509 certificates for authentication purposes.
For example, a single private/public key pair could be used to define
cluster membership, enabling authentication and encryption of all
intra-cluster communication. (Lack of certification from a CA matters
less in such a context.) For such use, generating the key pair at
package installation time when preparing system images for use in the
cluster is reasonable. For other use cases, it is necessary to generate
the key pair before the service is started for the first time, see
&lt;&lt;sect-Defensive_Coding-Tasks-Packaging-Certificates-Service&gt;&gt;,
and [Packaging:Initial Service
Setup](https://fedoraproject.org/wiki/Packaging:Initial_Service_Setup\&#35;Generating_Self-Signed_Certificates).

:::: important
::: title
:::

The way the key is generated may not be suitable for key material of
critical value. (\[command\]&#96;openssl genrsa&#96; uses, but does not
require, entropy from a physical source of randomness, among other
things.) Such keys should be stored in a hardware security module if
possible, and generated from random bits reserved for this purpose
derived from a non-deterministic physical source.
::::

In the spec file, we define two RPM variables which contain the names of
the files used to store the private and public key, and the user name
for the service:

``` bash
\&#35; Name of the user owning the file with the private key
%define tlsuser %{name}
\&#35; Name of the directory which contains the key and certificate files
%define tlsdir %{_sysconfdir}/%{name}
%define tlskey %{tlsdir}/%{name}.key
%define tlscert %{tlsdir}/%{name}.crt
```

These variables likely need adjustment based on the needs of the
package.

Typically, the file with the private key needs to be owned by the system
user which needs to read it, &#96;%{tlsuser}&#96; (not &#96;root&#96;).
In order to avoid races, if the &#42;directory&#42; &#96;%{tlsdir}&#96;
is &#42;owned by the services user&#42;, you should use the code in
&lt;&lt;ex-Defensive_Coding-Packaging-Certificates-Owned&gt;&gt;. The
invocation of \[application\]&#42;su&#42; with the \[option\]&#96;-s
/bin/bash&#96; argument is necessary in case the login shell for the
user has been disabled.

:::: {#ex-Defensive_Coding-Packaging-Certificates-Owned .example}
::: title
Creating a key pair in a user-owned directory
:::

``` bash
%post
if [ $1 -eq 1 ] ; then
if ! test -e %{tlskey} ; then
su -s /bin/bash \
-c 'umask 077 \&amp;\&amp; openssl genrsa -out %{tlskey} 2048 2\&gt;/dev/null' \
%{tlsuser}
fi
if ! test -e %{tlscert} ; then
cn='Automatically generated certificate for the %{tlsuser} service'
req_args='-key %{tlskey} -out %{tlscert} -days 7305 -subj \'/CN=$cn/\''
su -s /bin/bash \
-c 'openssl req -new -x509 -extensions usr_cert $req_args' \
%{tlsuser}
fi
fi

%files
%dir %attr(0755,%{tlsuser},%{tlsuser]) %{tlsdir}
%ghost %attr(0600,%{tlsuser},%{tlsuser}) %config(noreplace) %{tlskey}
%ghost %attr(0644,%{tlsuser},%{tlsuser}) %config(noreplace) %{tlscert}
```
::::

The files containing the key material are marked as ghost configuration
files. This ensures that they are tracked in the RPM database as
associated with the package, but RPM will not create them when the
package is installed and not verify their contents (the
&#96;%ghost&#96;), or delete the files when the package is uninstalled
(the &#96;%config(noreplace)&#96; part).

If the &#42;directory&#42; &#96;%{tlsdir}&#96; &#42;is owned by&#42;
&#96;root&#96;, use the code in
&lt;&lt;ex-Defensive_Coding-Packaging-Certificates-Unowned&gt;&gt;.

:::: {#ex-Defensive_Coding-Packaging-Certificates-Unowned .example}
::: title
Creating a key pair in a &#96;root&#96;-owned directory
:::

``` bash
%post
if [ $1 -eq 1 ] ; then
if ! test -e %{tlskey} ; then
(umask 077 \&amp;\&amp; openssl genrsa -out %{tlskey} 2048 2\&gt;/dev/null)
chown %{tlsuser} %{tlskey}
fi
if ! test -e %{tlscert} ; then
cn='Automatically generated certificate for the %{tlsuser} service'
openssl req -new -x509 -extensions usr_cert \
-key %{tlskey} -out %{tlscert} -days 7305 -subj '/CN=$cn/'
fi
fi

%files
%dir %attr(0755,root,root]) %{tlsdir}
%ghost %attr(0600,%{tlsuser},%{tlsuser}) %config(noreplace) %{tlskey}
%ghost %attr(0644,root,root) %config(noreplace) %{tlscert}
```
::::

In order for this to work, the package which generates the keys must
require the \[application\]&#42;openssl&#42; package. If the user which
owns the key file is generated by a different package, the package
generating the certificate must specify a &#96;Requires(pre):&#96; on
the package which creates the user. This ensures that the user account
will exist when it is needed for the \[application\]&#42;su&#42; or
\[application\]&#42;chmod&#42; invocation.

## Generating X.509 Self-signed Certificates before Service Start {#sect-Defensive_Coding-Tasks-Packaging-Certificates-Service}

An alternative way to automatically provide an X.509 key pair is to
create it just before the service is started for the first time. This
ensures that installation images which are created from installed RPM
packages receive different key material. Creating the key pair at
package installation time (see
&lt;&lt;sect-Defensive_Coding-Tasks-Packaging-Certificates&gt;&gt;)
would put the key into the image, which may or may not make sense.

:::: important
::: title
:::

The caveats about the way the key is generated in
&lt;&lt;sect-Defensive_Coding-Tasks-Packaging-Certificates&gt;&gt; apply
to this procedure as well.
::::

Generating key material before service start may happen very early
during boot, when the kernel randomness pool has not yet been
initialized. Currently, the only way to check for the initialization is
to look for the kernel message &#96;random: nonblocking pool is
initialized&#96;, or ensure that the application used for generating the
keys is utilizing the &#96;getrandom()&#96; system call.

In theory, it is also possible to use an application which reads from
&#96;/dev/random&#96; while generating the key material (instead of
&#96;/dev/urandom&#96;), but this can block not just during the boot
process, but also much later at run time, and generally results in a
poor user experience.

The requirements for generating such keys is documented at
[Packaging:Initial Service
Setup](https://fedoraproject.org/wiki/Packaging:Initial_Service_Setup\&#35;Generating_Self-Signed_Certificates).

&#42; Implementing Security Features :experimental: :toc:

# Authentication and Authorization {#_authentication_and_authorization}

## Authenticating Servers {#sect-Defensive_Coding-Authentication-Server}

When connecting to a server, a client has to make sure that it is
actually talking to the server it expects. There are two different
aspects, securing the network path, and making sure that the expected
user runs the process on the target host. There are several ways to
ensure that:

&#42; The server uses a TLS certificate which is valid according to the
web browser public key infrastructure, and the client verifies the
certificate and the host name.

&#42; The server uses a TLS certificate which is expected by the client
(perhaps it is stored in a configuration file read by the client). In
this case, no host name checking is required.

&#42; On Linux, UNIX domain sockets (of the &#96;PF_UNIX&#96; protocol
family, sometimes called &#96;PF_LOCAL&#96;) are restricted by file
system permissions. If the server socket path is not world-writable, the
server identity cannot be spoofed by local users.

&#42; Port numbers less than 1024 (&#42;trusted ports&#42;) can only be
used by &#96;root&#96;, so if a UDP or TCP server is running on the
local host and it uses a trusted port, its identity is assured. (Not all
operating systems enforce the trusted ports concept, and the network
might not be trusted, so it is only useful on the local system.)

[Transport Layer Security (TLS)](features/Features-TLS.xml) is the
recommended way for securing connections over untrusted networks.

If the server port number is 1024 is higher, a local user can
impersonate the process by binding to this socket, perhaps after
crashing the real server by exploiting a denial-of-service
vulnerability.

## Host-based Authentication {#sect-Defensive_Coding-Authentication-Host_based}

Host-based authentication uses access control lists (ACLs) to accept or
deny requests from clients. This authentication method comes in two
flavors: IP-based (or, more generally, address-based) and name-based
(with the name coming from DNS or &#96;/etc/hosts&#96;). IP-based ACLs
often use prefix notation to extend access to entire subnets. Name-based
ACLs sometimes use wildcards for adding groups of hosts (from entire DNS
subtrees). (In the SSH context, host-based authentication means
something completely different and is not covered in this section.)

Host-based authentication trust the network and may not offer sufficient
granularity, so it has to be considered a weak form of authentication.
On the other hand, IP-based authentication can be made extremely robust
and can be applied very early in input processing, so it offers an
opportunity for significantly reducing the number of potential attackers
for many services.

The names returned by &#96;gethostbyaddr&#96; and &#96;getnameinfo&#96;
functions cannot be trusted. (DNS PTR records can be set to arbitrary
values, not just names belong to the address owner.) If these names are
used for ACL matching, a forward lookup using &#96;gethostbyaddr&#96; or
&#96;getaddrinfo&#96; has to be performed. The name is only valid if the
original address is found among the results of the forward lookup
(&#42;double-reverse lookup&#42;).

An empty ACL should deny all access (deny-by-default). If empty ACLs
permits all access, configuring any access list must switch to
deny-by-default for all unconfigured protocols, in both name-based and
address-based variants.

Similarly, if an address or name is not matched by the list, it should
be denied. However, many implementations behave differently, so the
actual behavior must be documented properly.

IPv6 addresses can embed IPv4 addresses. There is no universally correct
way to deal with this ambiguity. The behavior of the ACL implementation
should be documented.

## UNIX Domain Socket Authentication {#sect-Defensive_Coding-Authentication-UNIX_Domain}

UNIX domain sockets (with address family &#96;AF_UNIX&#96; or
&#96;AF_LOCAL&#96;) are restricted to the local host and offer a special
authentication mechanism: credentials passing.

Nowadays, most systems support the &#96;SO_PEERCRED&#96; (Linux) or
&#96;LOCAL_PEERCRED&#96; (FreeBSD) socket options, or the
&#96;getpeereid&#96; (other BSDs, OS X). These interfaces provide direct
access to the (effective) user ID on the other end of a domain socket
connect, without cooperation from the other end.

Historically, credentials passing was implemented using ancillary data
in the &#96;sendmsg&#96; and &#96;recvmsg&#96; functions. On some
systems, only credentials data that the peer has explicitly sent can be
received, and the kernel checks the data for correctness on the sending
side. This means that both peers need to deal with ancillary data.
Compared to that, the modern interfaces are easier to use. Both sets of
interfaces vary considerably among UNIX-like systems, unfortunately.

If you want to authenticate based on supplementary groups, you should
obtain the user ID using one of these methods, and look up the list of
supplementary groups using &#96;getpwuid&#96; (or &#96;getpwuid_r&#96;)
and &#96;getgrouplist&#96;. Using the PID and information from
&#96;/proc/PID/status&#96; is prone to race conditions and insecure.

## &#96;AF_NETLINK&#96; Authentication of Origin {#sect-Defensive_Coding-Authentication-Netlink}

Netlink messages are used as a high-performance data transfer mechanism
between the kernel and the user space. Traditionally, they are used to
exchange information related to the network stack, such as routing table
entries.

When processing Netlink messages from the kernel, it is important to
check that these messages actually originate from the kernel, by
checking that the port ID (or PID) field &#96;nl_pid&#96; in the
&#96;sockaddr_nl&#96; structure is &#96;0&#96;. (This structure can be
obtained using &#96;recvfrom&#96; or &#96;recvmsg&#96;, it is different
from the &#96;nlmsghdr&#96; structure.) The kernel does not prevent
other processes from sending unicast Netlink messages, but the
&#96;nl_pid&#96; field in the sender's socket address will be non-zero
in such cases.

Applications should not use &#96;AF_NETLINK&#96; sockets as an IPC
mechanism among processes, but prefer UNIX domain sockets for this
tasks.

# Transport Layer Security (TLS) {#_transport_layer_security_tls}

Transport Layer Security (TLS, formerly Secure Sockets Layer/SSL) is the
recommended way to to protect integrity and confidentiality while data
is transferred over an untrusted network connection, and to identify the
endpoint. At this chapter we describe the available libraries in Fedora
as well as known pitfalls, and safe ways to write applications with
them.

When using any library, in addition to this guide, it is recommended to
consult the library\' documentation.

&#42; [NSS
documentation](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS)

&#42; [GnuTLS documentation](http://www.gnutls.org/manual/)

&#42; [OpenSSL documentation](https://www.openssl.org/docs/)

&#42; [OpenJDK
documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html)

## Common Pitfalls {#sect-Defensive_Coding-TLS-Pitfalls}

TLS implementations are difficult to use, and most of them lack a clean
API design. The following sections contain implementation-specific
advice, and some generic pitfalls are mentioned below.

&#42; Most TLS implementations have questionable default TLS cipher
suites. Most of them enable anonymous Diffie-Hellman key exchange (but
we generally want servers to authenticate themselves). Many do not
disable ciphers which are subject to brute-force attacks because of
restricted key lengths. Some even disable all variants of AES in the
default configuration.

\+ When overriding the cipher suite defaults, it is recommended to
disable all cipher suites which are not present on a whitelist, instead
of simply enabling a list of cipher suites. This way, if an algorithm is
disabled by default in the TLS implementation in a future security
update, the application will not re-enable it.

&#42; The name which is used in certificate validation must match the
name provided by the user or configuration file. No host name
canonicalization or IP address lookup must be performed.

&#42; The TLS handshake has very poor performance if the TCP Nagle
algorithm is active. You should switch on the &#96;TCP_NODELAY&#96;
socket option (at least for the duration of the handshake), or use the
Linux-specific &#96;TCP_CORK&#96; option.

\+

:::: {#ex-Defensive_Coding-TLS-Nagle .example}
::: title
Deactivating the TCP Nagle algorithm
:::

``` c
```
::::

&#42; Implementing proper session resumption decreases handshake
overhead considerably. This is important if the upper-layer protocol
uses short-lived connections (like most application of HTTPS).

&#42; Both client and server should work towards an orderly connection
shutdown, that is send &#96;close_notify&#96; alerts and respond to
them. This is especially important if the upper-layer protocol does not
provide means to detect connection truncation (like some uses of HTTP).

&#42; When implementing a server using event-driven programming, it is
important to handle the TLS handshake properly because it includes
multiple network round-trips which can block when an ordinary TCP
&#96;accept&#96; would not. Otherwise, a client which fails to complete
the TLS handshake for some reason will prevent the server from handling
input from other clients.

&#42; Unlike regular file descriptors, TLS connections cannot be passed
between processes. Some TLS implementations add additional restrictions,
and TLS connections generally cannot be used across &#96;fork&#96;
function calls (see [&#96;fork&#96; as a Primitive for
Parallelism](tasks/Tasks-Processes.adoc&#35;sect-Defensive_Coding-Tasks-Processes-Fork-Parallel)).

### OpenSSL Pitfalls {#sect-Defensive_Coding-TLS-OpenSSL}

Some OpenSSL function use &#42;tri-state return values&#42;. Correct
error checking is extremely important. Several functions return
&#96;int&#96; values with the following meaning:

&#42; The value &#96;1&#96; indicates success (for example, a successful
signature verification).

&#42; The value &#96;0&#96; indicates semantic failure (for example, a
signature verification which was unsuccessful because the signing
certificate was self-signed).

&#42; The value &#96;-1&#96; indicates a low-level error in the system,
such as failure to allocate memory using &#96;malloc&#96;.

Treating such tri-state return values as booleans can lead to security
vulnerabilities. Note that some OpenSSL functions return boolean results
or yet another set of status indicators. Each function needs to be
checked individually.

Recovering precise error information is difficult.
&lt;&lt;ex-Defensive_Coding-TLS-OpenSSL-Errors&gt;&gt; shows how to
obtain a more precise error code after a function call on an
&#96;SSL&#96; object has failed. However, there are still cases where no
detailed error information is available (e.g., if &#96;SSL_shutdown&#96;
fails due to a connection teardown by the other end).

:::: {#ex-Defensive_Coding-TLS-OpenSSL-Errors .example}
::: title
Obtaining OpenSSL error codes
:::

``` c
```
::::

The &#96;OPENSSL_config&#96; function is documented to never fail. In
reality, it can terminate the entire process if there is a failure
accessing the configuration file. An error message is written to
standard error, but which might not be visible if the function is called
from a daemon process.

OpenSSL contains two separate ASN.1 DER decoders. One set of decoders
operate on BIO handles (the input/output stream abstraction provided by
OpenSSL); their decoder function names start with &#96;d2i\_&#96; and
end in &#96;\_fp&#96; or &#96;\_bio&#96; (e.g., &#96;d2i_X509_fp&#96; or
&#96;d2i_X509_bio&#96;). These decoders must not be used for parsing
data from untrusted sources; instead, the variants without the
&#96;\_fp&#96; and &#96;\_bio&#96; (e.g., &#96;d2i_X509&#96;) shall be
used. The BIO variants have received considerably less testing and are
not very robust.

For the same reason, the OpenSSL command line tools (such as
\[command\]&#96;openssl x509&#96;) are generally generally less robust
than the actual library code. They use the BIO functions internally, and
not the more robust variants.

The command line tools do not always indicate failure in the exit status
of the \[application\]&#42;openssl&#42; process. For instance, a
verification failure in \[command\]&#96;openssl verify&#96; result in an
exit status of zero.

OpenSSL command-line commands, such as \[command\]&#96;openssl
genrsa&#96;, do not ensure that physical entropy is used for key
generation---they obtain entropy from &#96;/dev/urandom&#96; and other
sources, but not from &#96;/dev/random&#96;. This can result in weak
keys if the system lacks a proper entropy source (e.g., a virtual
machine with solid state storage). Depending on local policies, keys
generated by these OpenSSL tools should not be used in high-value,
critical functions.

The OpenSSL server and client applications (\[command\]&#96;openssl
s_client&#96; and \[command\]&#96;openssl s_server&#96;) are debugging
tools and should &#42;never&#42; be used as generic clients. For
instance, the \[application\]&#42;s_client&#42; tool reacts in a
surprising way to lines starting with &#96;R&#96; and &#96;Q&#96;.

OpenSSL allows application code to access private key material over
documented interfaces. This can significantly increase the part of the
code base which has to undergo security certification.

### GnuTLS Pitfalls {#sect-Defensive_Coding-TLS-Pitfalls-GnuTLS}

Older versions of GnuTLS had several peculiarities described in previous
versions of this guide; as of GnuTLS 3.3.10, these issues are no longer
applicable.

### OpenJDK Pitfalls {#sect-Defensive_Coding-TLS-Pitfalls-OpenJDK}

The Java cryptographic framework is highly modular. As a result, when
you request an object implementing some cryptographic functionality, you
cannot be completely sure that you end up with the well-tested, reviewed
implementation in OpenJDK.

OpenJDK (in the source code as published by Oracle) and other
implementations of the Java platform require that the system
administrator has installed so-called &#42;unlimited strength
jurisdiction policy files&#42;. Without this step, it is not possible to
use the secure algorithms which offer sufficient cryptographic strength.
Most downstream redistributors of OpenJDK remove this requirement.

Some versions of OpenJDK use &#96;/dev/random&#96; as the randomness
source for nonces and other random data which is needed for TLS
operation, but does not actually require physical randomness. As a
result, TLS applications can block, waiting for more bits to become
available in &#96;/dev/random&#96;.

### NSS Pitfalls {#sect-Defensive_Coding-TLS-Pitfalls-NSS}

NSS was not designed to be used by other libraries which can be linked
into applications without modifying them. There is a lot of global
state. There does not seem to be a way to perform required NSS
initialization without race conditions.

If the NSPR descriptor is in an unexpected state, the
&#96;SSL_ForceHandshake&#96; function can succeed, but no TLS handshake
takes place, the peer is not authenticated, and subsequent data is
exchanged in the clear.

NSS disables itself if it detects that the process underwent a
&#96;fork&#96; after the library has been initialized. This behavior is
required by the PKCS&#35;11 API specification.

## TLS Clients {#sect-Defensive_Coding-TLS-Client}

Secure use of TLS in a client generally involves all of the following
steps. (Individual instructions for specific TLS implementations follow
in the next sections.)

&#42; The client must configure the TLS library to use a set of trusted
root certificates. These certificates are provided by the system in
various formats and files. These are documented in
&#96;update-ca-trust&#96; man page in Fedora. Portable applications
should not hard-code any paths; they should rely on APIs which set the
default for the system trust store.

&#42; The client selects sufficiently strong cryptographic primitives
and disables insecure ones (such as no-op encryption). Compression
support and SSL version 3 or lower must be disabled (including the
SSLv2-compatible handshake).

&#42; The client initiates the TLS connection. The Server Name
Indication extension should be used if supported by the TLS
implementation. Before switching to the encrypted connection state, the
contents of all input and output buffers must be discarded.

&#42; The client needs to validate the peer certificate provided by the
server, that is, the client must check that there is a cryptographically
protected chain from a trusted root certificate to the peer certificate.
(Depending on the TLS implementation, a TLS handshake can succeed even
if the certificate cannot be validated.)

&#42; The client must check that the configured or user-provided server
name matches the peer certificate provided by the server.

It is safe to provide users detailed diagnostics on certificate
validation failures. Other causes of handshake failures and, generally
speaking, any details on other errors reported by the TLS implementation
(particularly exception tracebacks), must not be divulged in ways that
make them accessible to potential attackers. Otherwise, it is possible
to create decryption oracles.

:::: important
::: title
:::

Depending on the application, revocation checking (against certificate
revocations lists or via OCSP) and session resumption are important
aspects of production-quality client. These aspects are not yet covered.
::::

### Implementation TLS Clients With OpenSSL {#_implementation_tls_clients_with_openssl}

In the following code, the error handling is only exploratory. Proper
error handling is required for production use, especially in libraries.

The OpenSSL library needs explicit initialization (see
&lt;&lt;ex-Defensive_Coding-TLS-OpenSSL-Init&gt;&gt;).

:::: {#ex-Defensive_Coding-TLS-OpenSSL-Init .example}
::: title
OpenSSL library initialization
:::

``` c
```
::::

After that, a context object has to be created, which acts as a factory
for connection objects
(&lt;&lt;ex-Defensive_Coding-TLS-Client-OpenSSL-CTX&gt;&gt;). We use an
explicit cipher list so that we do not pick up any strange ciphers when
OpenSSL is upgraded. The actual version requested in the client hello
depends on additional restrictions in the OpenSSL library. If possible,
you should follow the example code and use the default list of trusted
root certificate authorities provided by the system because you would
have to maintain your own set otherwise, which can be cumbersome.

:::: {#ex-Defensive_Coding-TLS-Client-OpenSSL-CTX .example}
::: title
OpenSSL client context creation
:::

``` c
```
::::

A single context object can be used to create multiple connection
objects. It is safe to use the same &#96;SSL_CTX&#96; object for
creating connections concurrently from multiple threads, provided that
the &#96;SSL_CTX&#96; object is not modified (e.g., callbacks must not
be changed).

After creating the TCP socket and disabling the Nagle algorithm (per
&lt;&lt;ex-Defensive_Coding-TLS-Nagle&gt;&gt;), the actual connection
object needs to be created, as show in
&lt;&lt;ex-Defensive_Coding-TLS-Client-OpenSSL-CTX&gt;&gt;. If the
handshake started by &#96;SSL_connect&#96; fails, the
&#96;ssl_print_error_and_exit&#96; function from
&lt;&lt;ex-Defensive_Coding-TLS-OpenSSL-Errors&gt;&gt; is called.

The &#96;certificate_validity_override&#96; function provides an
opportunity to override the validity of the certificate in case the
OpenSSL check fails. If such functionality is not required, the call can
be removed, otherwise, the application developer has to implement it.

The host name passed to the functions &#96;SSL_set_tlsext_host_name&#96;
and &#96;X509_check_host&#96; must be the name that was passed to
&#96;getaddrinfo&#96; or a similar name resolution function. No host
name canonicalization must be performed. The &#96;X509_check_host&#96;
function used in the final step for host name matching is currently only
implemented in OpenSSL 1.1, which is not released yet. In case host name
matching fails, the function &#96;certificate_host_name_override&#96; is
called. This function should check user-specific certificate store, to
allow a connection even if the host name does not match the certificate.
This function has to be provided by the application developer. Note that
the override must be keyed by both the certificate &#42;and&#42; the
host name.

:::: {#ex-Defensive_Coding-TLS-Client-OpenSSL-Connect .example}
::: title
Creating a client connection using OpenSSL
:::

``` c
```
::::

The connection object can be used for sending and receiving data, as in
&lt;&lt;ex-Defensive_Coding-TLS-OpenSSL-Connection-Use&gt;&gt;. It is
also possible to create a &#96;BIO&#96; object and use the &#96;SSL&#96;
object as the underlying transport, using &#96;BIO_set_ssl&#96;.

:::: {#ex-Defensive_Coding-TLS-OpenSSL-Connection-Use .example}
::: title
Using an OpenSSL connection to send and receive data
:::

``` c
```
::::

When it is time to close the connection, the &#96;SSL_shutdown&#96;
function needs to be called twice for an orderly, synchronous connection
termination
(&lt;&lt;ex-Defensive_Coding-TLS-OpenSSL-Connection-Close&gt;&gt;). This
exchanges &#96;close_notify&#96; alerts with the server. The additional
logic is required to deal with an unexpected &#96;close_notify&#96; from
the server. Note that is necessary to explicitly close the underlying
socket after the connection object has been freed.

:::: {#ex-Defensive_Coding-TLS-OpenSSL-Connection-Close .example}
::: title
Closing an OpenSSL connection in an orderly fashion
:::

``` c
```
::::

&lt;&lt;ex-Defensive_Coding-TLS-OpenSSL-Context-Close&gt;&gt; shows how
to deallocate the context object when it is no longer needed because no
further TLS connections will be established.

:::: {#ex-Defensive_Coding-TLS-OpenSSL-Context-Close .example}
::: title
Closing an OpenSSL connection in an orderly fashion
:::

``` c
```
::::

### Implementation TLS Clients With GnuTLS {#sect-Defensive_Coding-TLS-Client-GnuTLS}

This section describes how to implement a TLS client with full
certificate validation (but without certificate revocation checking).
Note that the error handling in is only exploratory and needs to be
replaced before production use.

Before setting up TLS connections, a credentials objects has to be
allocated and initialized with the set of trusted root CAs
(&lt;&lt;ex-Defensive_Coding-TLS-Client-GNUTLS-Credentials&gt;&gt;).

:::: {#ex-Defensive_Coding-TLS-Client-GNUTLS-Credentials .example}
::: title
Initializing a GnuTLS credentials structure
:::

``` c
```
::::

After the last TLS connection has been closed, this credentials object
should be freed:

``` c
```

During its lifetime, the credentials object can be used to initialize
TLS session objects from multiple threads, provided that it is not
changed.

Once the TCP connection has been established, the Nagle algorithm should
be disabled (see &lt;&lt;ex-Defensive_Coding-TLS-Nagle&gt;&gt;). After
that, the socket can be associated with a new GnuTLS session object. The
previously allocated credentials object provides the set of root CAs.
Then the TLS handshake must be initiated. This is shown in
&lt;&lt;ex-Defensive_Coding-TLS-Client-GNUTLS-Connect&gt;&gt;.

:::: {#ex-Defensive_Coding-TLS-Client-GNUTLS-Connect .example}
::: title
Establishing a TLS client connection using GnuTLS
:::

``` c
```
::::

After the handshake has been completed, the server certificate needs to
be verified against the server's hostname
(&lt;&lt;ex-Defensive_Coding-TLS-Client-GNUTLS-Verify&gt;&gt;). In the
example, the user-defined &#96;certificate_validity_override&#96;
function is called if the verification fails, so that a separate,
user-specific trust store can be checked. This function call can be
omitted if the functionality is not needed.

:::: {#ex-Defensive_Coding-TLS-Client-GNUTLS-Verify .example}
::: title
Verifying a server certificate using GnuTLS
:::

``` c
```
::::

An established TLS session can be used for sending and receiving data,
as in &lt;&lt;ex-Defensive_Coding-TLS-GNUTLS-Use&gt;&gt;.

:::: {#ex-Defensive_Coding-TLS-GNUTLS-Use .example}
::: title
Using a GnuTLS session
:::

``` c
```
::::

In order to shut down a connection in an orderly manner, you should call
the &#96;gnutls_bye&#96; function. Finally, the session object can be
deallocated using &#96;gnutls_deinit&#96; (see
&lt;&lt;ex-Defensive_Coding-TLS-GNUTLS-Disconnect&gt;&gt;).

:::: {#ex-Defensive_Coding-TLS-GNUTLS-Disconnect .example}
::: title
Closing a GnuTLS session in an orderly fashion
:::

``` c
```
::::

### Implementing TLS Clients With OpenJDK {#sect-Defensive_Coding-TLS-Client-OpenJDK}

The examples below use the following cryptographic-related classes:

``` java
```

If compatibility with OpenJDK 6 is required, it is necessary to use the
internal class &#96;sun.security.util.HostnameChecker&#96;. (The public
OpenJDK API does not provide any support for dissecting the subject
distinguished name of an X.509 certificate, so a custom-written DER
parser is needed---or we have to use an internal class, which we do
below.) In OpenJDK 7, the &#96;setEndpointIdentificationAlgorithm&#96;
method was added to the &#96;javax.net.ssl.SSLParameters&#96; class,
providing an official way to implement host name checking.

TLS connections are established using an &#96;SSLContext&#96; instance.
With a properly configured OpenJDK installation, the &#96;SunJSSE&#96;
provider uses the system-wide set of trusted root certificate
authorities, so no further configuration is necessary. For backwards
compatibility with OpenJDK6, the &#96;TLSv1&#96; provider has to be
supported as a fall-back option. This is shown in
&lt;&lt;ex-Defensive_Coding-TLS-Client-OpenJDK-Context&gt;&gt;.

:::: {#ex-Defensive_Coding-TLS-Client-OpenJDK-Context .example}
::: title
Setting up an &#96;SSLContext&#96; for OpenJDK TLS clients
:::

``` java
```
::::

In addition to the context, a TLS parameter object will be needed which
adjusts the cipher suites and protocols
(&lt;&lt;ex-Defensive_Coding-TLS-OpenJDK-Parameters&gt;&gt;). Like the
context, these parameters can be reused for multiple TLS connections.

:::: {#ex-Defensive_Coding-TLS-OpenJDK-Parameters .example}
::: title
Setting up &#96;SSLParameters&#96; for TLS use with OpenJDK
:::

``` java
```
::::

As initialized above, the parameter object does not yet require host
name checking. This has to be enabled separately, and this is only
supported by OpenJDK 7 and later:

``` java
```

All application protocols can use the &#96;\'HTTPS\'&#96; algorithm.
(The algorithms have minor differences with regard to wildcard handling,
which should not matter in practice.)

&lt;&lt;ex-Defensive_Coding-TLS-Client-OpenJDK-Connect&gt;&gt; shows how
to establish the connection. Before the handshake is initialized, the
protocol and cipher configuration has to be performed, by applying the
parameter object &#96;params&#96;. (After this point, changes to
&#96;params&#96; will not affect this TLS socket.) As mentioned
initially, host name checking requires using an internal API on OpenJDK
6.

:::: {#ex-Defensive_Coding-TLS-Client-OpenJDK-Connect .example}
::: title
Establishing a TLS connection with OpenJDK
:::

``` java
```
::::

Starting with OpenJDK 7, the last lines can be omitted, provided that
host name verification has been enabled by calling the
&#96;setEndpointIdentificationAlgorithm&#96; method on the
&#96;params&#96; object (before it was applied to the socket).

The TLS socket can be used as a regular socket, as shown in
&lt;&lt;ex-Defensive_Coding-TLS-Client-OpenJDK-Use&gt;&gt;.

:::: {#ex-Defensive_Coding-TLS-Client-OpenJDK-Use .example}
::: title
Using a TLS client socket in OpenJDK
:::

``` java
```
::::

#### Overriding server certificate validation with OpenJDK 6 {#_overriding_server_certificate_validation_with_openjdk_6}

Overriding certificate validation requires a custom trust manager. With
OpenJDK 6, the trust manager lacks information about the TLS session,
and to which server the connection is made. Certificate overrides have
to be tied to specific servers (host names). Consequently, different
&#96;TrustManager&#96; and &#96;SSLContext&#96; objects have to be used
for different servers.

In the trust manager shown in
&lt;&lt;ex-Defensive_Coding-TLS-Client-MyTrustManager&gt;&gt;, the
server certificate is identified by its SHA-256 hash.

:::: {#ex-Defensive_Coding-TLS-Client-MyTrustManager .example}
::: title
A customer trust manager for OpenJDK TLS clients
:::

``` java
```
::::

This trust manager has to be passed to the &#96;init&#96; method of the
&#96;SSLContext&#96; object, as show in
&lt;&lt;ex-Defensive_Coding-TLS-Client-Context_For_Cert&gt;&gt;.

:::: {#ex-Defensive_Coding-TLS-Client-Context_For_Cert .example}
::: title
Using a custom TLS trust manager with OpenJDK
:::

``` java
```
::::

When certificate overrides are in place, host name verification should
not be performed because there is no security requirement that the host
name in the certificate matches the host name used to establish the
connection (and it often will not). However, without host name
verification, it is not possible to perform transparent fallback to
certification validation using the system certificate store.

The approach described above works with OpenJDK 6 and later versions.
Starting with OpenJDK 7, it is possible to use a custom subclass of the
&#96;javax.net.ssl.X509ExtendedTrustManager&#96; class. The OpenJDK TLS
implementation will call the new methods, passing along TLS session
information. This can be used to implement certificate overrides as a
fallback (if certificate or host name verification fails), and a trust
manager object can be used for multiple servers because the server
address is available to the trust manager.

### Implementing TLS Clients With NSS {#sect-Defensive_Coding-TLS-Client-NSS}

The following code shows how to implement a simple TLS client using NSS.
These instructions apply to NSS version 3.14 and later. Versions before
3.14 need different initialization code.

Keep in mind that the error handling needs to be improved before the
code can be used in production.

Using NSS needs several header files, as shown in
&lt;&lt;ex-Defensive_Coding-TLS-NSS-Includes&gt;&gt;.

:::: {#ex-Defensive_Coding-TLS-NSS-Includes .example}
::: title
Include files for NSS
:::

``` c
```
::::

Initializing the NSS library is shown in
&lt;&lt;ex-Defensive_Coding-TLS-NSS-Init&gt;&gt;. This initialization
procedure overrides global state. We only call
&#96;NSS_SetDomesticPolicy&#96; if there are no strong ciphers
available, assuming that it has already been called otherwise. This
avoids overriding the process-wide cipher suite policy unnecessarily.

The simplest way to configured the trusted root certificates involves
loading the &#96;libnssckbi.so&#96; NSS module with a call to the
&#96;SECMOD_LoadUserModule&#96; function. The root certificates are
compiled into this module. (The PEM module for NSS,
&#96;libnsspem.so&#96;, offers a way to load trusted CA certificates
from a file.)

:::: {#ex-Defensive_Coding-TLS-NSS-Init .example}
::: title
Initializing the NSS library
:::

``` c
```
::::

Some of the effects of the initialization can be reverted with the
following function calls:

``` c
```

After NSS has been initialized, the TLS connection can be created
(&lt;&lt;ex-Defensive_Coding-TLS-Client-NSS-Connect&gt;&gt;). The
internal &#96;PR_ImportTCPSocket&#96; function is used to turn the POSIX
file descriptor &#96;sockfd&#96; into an NSPR file descriptor. (This
function is de-facto part of the NSS public ABI, so it will not go
away.) Creating the TLS-capable file descriptor requires a
&#42;model&#42; descriptor, which is configured with the desired set of
protocols. The model descriptor is not needed anymore after TLS support
has been activated for the existing connection descriptor.

The call to &#96;SSL_BadCertHook&#96; can be omitted if no mechanism to
override certificate verification is needed. The
&#96;bad_certificate&#96; function must check both the host name
specified for the connection and the certificate before granting the
override.

Triggering the actual handshake requires three function calls,
&#96;SSL_ResetHandshake&#96;, &#96;SSL_SetURL&#96;, and
&#96;SSL_ForceHandshake&#96;. (If &#96;SSL_ResetHandshake&#96; is
omitted, &#96;SSL_ForceHandshake&#96; will succeed, but the data will
not be encrypted.) During the handshake, the certificate is verified and
matched against the host name.

:::: {#ex-Defensive_Coding-TLS-Client-NSS-Connect .example}
::: title
Creating a TLS connection with NSS
:::

``` c
```
::::

After the connection has been established,
&lt;&lt;ex-Defensive_Coding-TLS-NSS-Use&gt;&gt; shows how to use the
NSPR descriptor to communicate with the server.

:::: {#ex-Defensive_Coding-TLS-NSS-Use .example}
::: title
Using NSS for sending and receiving data
:::

``` c
```
::::

&lt;&lt;ex-Defensive_Coding-TLS-Client-NSS-Close&gt;&gt; shows how to
close the connection.

:::: {#ex-Defensive_Coding-TLS-Client-NSS-Close .example}
::: title
Closing NSS client connections
:::

``` c
```
::::

### Implementing TLS Clients With Python {#sect-Defensive_Coding-TLS-Client-Python}

The Python distribution provides a TLS implementation in the
&#96;ssl&#96; module (actually a wrapper around OpenSSL). The exported
interface is somewhat restricted, so that the client code shown below
does not fully implement the recommendations in
&lt;&lt;sect-Defensive_Coding-TLS-OpenSSL&gt;&gt;.

:::: important
::: title
:::

Currently, most Python function which accept &#96;<https://&#96>; URLs
or otherwise implement HTTPS support do not perform certificate
validation at all. (For example, this is true for the &#96;httplib&#96;
and &#96;xmlrpclib&#96; modules.) If you use HTTPS, you should not use
the built-in HTTP clients. The &#96;Curl&#96; class in the
&#96;curl&#96; module, as provided by the &#96;python-pycurl&#96;
package implements proper certificate validation.
::::

The &#96;ssl&#96; module currently does not perform host name checking
on the server certificate.
&lt;&lt;ex-Defensive_Coding-TLS-Client-Python-check_host_name&gt;&gt;
shows how to implement certificate matching, using the parsed
certificate returned by &#96;getpeercert&#96;.

:::: {#ex-Defensive_Coding-TLS-Client-Python-check_host_name .example}
::: title
Implementing TLS host name checking Python (without wildcard support)
:::

``` python
```
::::

To turn a regular, connected TCP socket into a TLS-enabled socket, use
the &#96;ssl.wrap_socket&#96; function. The function call in
&lt;&lt;ex-Defensive_Coding-TLS-Client-Python-Connect&gt;&gt; provides
additional arguments to override questionable defaults in OpenSSL and in
the Python module.

&#42; &#96;ciphers=\'HIGH:-aNULL:-eNULL:-PSK:RC4-SHA:RC4-MD5\'&#96;
selects relatively strong cipher suites with certificate-based
authentication. (The call to &#96;check_host_name&#96; function provides
additional protection against anonymous cipher suites.)

&#42; &#96;ssl_version=ssl.PROTOCOL_TLSv1&#96; disables SSL 2.0 support.
By default, the &#96;ssl&#96; module sends an SSL 2.0 client hello,
which is rejected by some servers. Ideally, we would request OpenSSL to
negotiated the most recent TLS version supported by the server and the
client, but the Python module does not allow this.

&#42; &#96;cert_reqs=ssl.CERT_REQUIRED&#96; turns on certificate
validation.

&#42; &#96;ca_certs=\'/etc/ssl/certs/ca-bundle.crt\'&#96; initializes
the certificate store with a set of trusted root CAs. Unfortunately, it
is necessary to hard-code this path into applications because the
default path in OpenSSL is not available through the Python
&#96;ssl&#96; module.

The &#96;ssl&#96; module (and OpenSSL) perform certificate validation,
but the certificate must be compared manually against the host name, by
calling the &#96;check_host_name&#96; defined above.

:::: {#ex-Defensive_Coding-TLS-Client-Python-Connect .example}
::: title
Establishing a TLS client connection with Python
:::

``` python
```
::::

After the connection has been established, the TLS socket can be used
like a regular socket:

``` python
```

Closing the TLS socket is straightforward as well:

``` python
```

# Hardware Security Modules and Smart Cards {#chap-Defensive_Coding-HSM}

Hardware Security Modules (HSMs) are specialized hardware intended to
protect private keys on server systems. They store internally the
private keys (e.g., RSA keys), and provide access to operations with the
keys without exposing the keys. That access, is provided using a
standardized API, which across Fedora is PKCS&#35;11.

Smart cards are small cards with a micro processor, often combined with
a USB reader resembling a USB stick. They are very similar in nature
with HSMs as they can also be used to protect private keys and are
almost universally accessed via the PKCS&#35;11 API. The main
distinguishers from HSMs is their inferior performance and often, the
available hardware protection mechanisms.

Typically a smart card or HSM relies on a shared library to provide
functionality. This shared library follows the PKCS&#35;11 API and thus
is often referred to as a PKCS&#35;11 module. In Fedora the
&#96;opensc&#96; shared module (&#96;opensc-pkcs11.so&#96;) can be used
for the majority of smart cards available in the market. By convention
these modules are located at &#96;/usr/lib64/pkcs11&#96;. They can be
used directly, or via a higher level library.

All the major crypto libraries (NSS, GnuTLS and OpenSSL in Fedora)
support hardware security modules and smart cards, by providing wrappers
over the PKCS&#35;11 API. However, the level of support varies, as well
as the ease of use of such modules and its integration to the overall
library API.

&#42; The PKCS&#35;11 API does provide an API to access HSMs or smart
cards, but does not provide any method of discovering which HSMs or
smart cards are available in the system. In Fedora and modules are
registered via [p11-kit configuration
files](https://p11-glue.freedesktop.org/doc/p11-kit/pkcs11-conf.html),
stored at &#96;/etc/pkcs11/modules/&#96;. For applications using
&#96;engine_pkcs11&#96; or GnuTLS the registered modules are available
without further configuration. Other applications will have to load the
&#96;p11-kit-proxy.so&#96; module.

&#42; Most crypto libraries support the [PKCS&#35;11 URLs
scheme](https://tools.ietf.org/html/rfc7512) to identify objects stored
in an HSM, however that support is not yet universal. Some support
transparent usage of PKCS&#35;11 objects, e.g., specifying a PKCS&#35;11
object instead of a file, while others require to use specialized APIs
for such objects.

&#42; Objects stored in an HSM or smart card can be protected with a
PIN. As such, libraries typically require to set a PIN handling function
for accessing private keys, or the PIN can be passed along with a
PKCS&#35;11 URL and the pin-value parameter.

&#42; Obtaining a Hardware Security Module, or including it on a
continuous integration testing is not always feasible. For testing
purposes smart cards supported by the OpenSC project can be used, as
well as software modules like &#96;softhsm&#96; which provides a tool to
setup a software HSM, and a PKCS&#35;11 library.

&#42; The PKCS&#35;11 API requires applications that use fork to
reinitialize the used PKCS&#35;11 modules. This is an uncommon
requirement, which has led to several bugs across applications in Fedora
which used PKCS&#35;11 directly. To make things more complicated
software PKCS&#35;11 module like &#96;softhsm&#96; do not require this
re-initialization leading to applications working against software
modules but failing with hardware modules or smart cards. The wrapper
PKCS&#35;11 APIs provided by NSS, GnuTLS and engine_pkcs11 (OpenSSL)
handle the reinitialization after fork requirement transparently.

## OpenSSL HSM Support {#sect-Defensive_Coding-HSM-OpenSSL}

OpenSSL does not have native support for PKCS&#35;11. It can provide
PKCS&#35;11 support through the OpenSC's project &#96;pkcs11&#96; engine
(formerly known as &#96;engine_pkcs11&#96;). As such software intended
to use HSMs, must utilize that engine.

Engine &#96;pkcs11&#96; supports loading stored objects via PKCS&#35;11
URLs. If no PKCS&#35;11 module is specified the engine will use the
system-wide registered modules via &#96;p11-kit-proxy.so&#96;.

The following example demonstrates the initialization of the pkcs11
engine and its usage to sign data.

:::: {#ex-Defensive_Coding-HSM-OpenSSL .example}
::: title
Signing data with HSM and OpenSSL
:::

``` c
```
::::

## GnuTLS HSM Support {#sect-Defensive_Coding-HSM-GNUTLS}

GnuTLS supports PKCS&#35;11 natively. Most of the API functions
accepting certificate files, can also accept PKCS&#35;11 URLs, thus
requiring minor or no modifications to applications in order to support
HSMs. In most cases applications must be modified to install a PIN
callback function.

The following example demonstrates the initialization of the pkcs11
engine and its usage to sign data.

:::: {#ex-Defensive_Coding-HSM-GNUTLS .example}
::: title
Signing data with HSM and GnuTLS
:::

``` c
```
::::

The PIN callback function can be either set globally as in the example
above or locally by utilizing functions such as
&#96;gnutls_privkey_set_pin_function&#96;. An example PIN callback
function is shown below.

:::: {#ex-Defensive_Coding-HSM-GNUTLS-PIN .example}
::: title
An example PIN callback with GNUTLS
:::

``` c
```
::::

## NSS HSM Support {#sect-Defensive_Coding-HSM-NSS}

NSS supports PKCS&#35;11 natively. In fact all NSS crypto operations,
including built-in operations, go through PKCS &#35;11 modules. NSS
provides its own software PKCS &#35;11 module called softoken. NSS
automatically loads any PKCS &#35;11 module specified in its module
database, which can be manipulated with the modutil command. NSS uses
the PKCS &#35;11 module that contains the requested keys to do the
crypto operations. As long as the application opens an NSS database and
properly sets a pin callback. If it runs with native NSS, it should be
able to use HSMs that provide PKCS &#35;11 modules. Modules can also be
loaded programmatically, though this is less common.

The following example demonstrates a typical NSS application for
signing.

:::: {#ex-Defensive_Coding-HSM-NSS .example}
::: title
Signing data with HSM and NSS
:::

``` c
```
::::

To use the example above with an HSM or smart card you will need to do
the following.

``` bash
\&#35; add your HSM or token library to an NSS database (in the sample code the database is
\&#35; located in the current directory'.')
$ modutil -add 'My HSM' -libfile ${path_to_pkcs11_file} -dbdir .
\&#35; Find the token name on your HSM
$ modutil -list -dbdir .
\&#35; find the cert on your token
$ certutil -L -h ${token_name} -d .
\&#35; pass the cert to your signing program
$ NSS_Sign_Example '${token_name}:${cert_name}'
```

:::: {#ex-Defensive_Coding-HSM-NSS-PIN .example}
::: title
An example PIN callback with NSS
:::

``` c
```
::::

# Revision History {#_revision_history}

&#96;1.8&#96;

:   Thu Jan 13 2021 Petr Bokoc (<pbokoc@gmail.com>)

&#42; Complete book cleanup &amp; publishing on docs.fedoraproject.org

&#96;1.7&#96;

:   Sat Sept 18. 2021 Huzaifa Sidhpurwala (<huzaifas@redhat.com>)

&#42; Add some C-library/syscall specific advice

&#96;1.6&#96;

:   Mon Oct 26 2020, Huzaifa Sidhpuwala (<huzaifas@redhat.com>)

&#42; Add section on misuse of Macros - <wmealing@redhat.com>

&#42; Add information about removing sensitive information from memory -
<huzaifas@redhat.com>

&#42; Update cryptographic recommendations for Python -
<ntait@redhat.com>

&#42; C-Allocators: various sections - <dueno@redhat.com>

&#96;1.5&#96;

:   Fri Dec 1 2017, Mirek Jahoda (<mjahoda@redhat.com>)

&#42; First release in AsciiDoc

&#42; Many updates in the crypto-related sections

&#42; Grammar and typography fixes

&#96;1.3-1&#96;

:   Mon Oct 13 2014, Florian Weimer (<fweimer@redhat.com>)

&#42; Go: Mention default value handling in deserialization

&#42; Shell: New chapter

&#96;1.2-1&#96;

:   Wed Jul 16 2014, Florian Weimer (<fweimer@redhat.com>)

&#42; C: Corrected the &#96;strncat&#96; example

&#42; C: Mention mixed signed/unsigned comparisons

&#42; C: Unsigned overflow checking example

&#42; C++: &#96;operator new\[\]&#96; has been fixed in GCC

&#42; C++: Additional material on &#96;std::string&#96;, iterators

&#42; OpenSSL: Mention \[command\]&#96;openssl genrsa&#96; entropy issue

&#42; Packaging: X.509 key generation

&#42; Go, Vala: Add short chapters

&#42; Serialization: Notes on fragmentation and reassembly

&#96;1.1-1&#96;

:   Tue Aug 27 2013, Eric Christensen (<sparks@redhat.com>)

&#42; Add a chapter which covers some Java topics.

&#42; Deserialization: Warn about Java's java.beans.XMLDecoder.

&#42; C: Correct the advice on array allocation ([bug
995595](https://bugzilla.redhat.com/show_bug.cgi?id=995595)).

&#42; C: Add material on global variables.

&#96;1.0-1&#96;

:   Thu May 09 2013, Eric Christensen (<sparks@redhat.com>)

&#42; Added more C and C++ examples.

&#42; TLS Client NSS: Rely on NSS 3.14 cipher suite defaults.

&#96;0-1&#96;

:   Thu Mar 7 2013, Eric Christensen (<sparks@redhat.com>)

&#42; Initial publication.
