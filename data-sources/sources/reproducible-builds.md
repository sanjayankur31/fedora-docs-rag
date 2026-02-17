The problem manifests as file having a different timestamp in a rebuild.
Example rpmdiff output:

    beesu-2.7-50.fc42.x86_64
    modified-\&#8230;\&#8230;\&#8230;.T /etc/security/console.apps/beesu
    modified-\&#8230;\&#8230;\&#8230;.T /usr/bin/beesu
    modified-\&#8230;\&#8230;\&#8230;.T /usr/lib/.build-id
    modified-\&#8230;\&#8230;\&#8230;.T /usr/lib/.build-id/d6
    modified-\&#8230;\&#8230;\&#8230;.T /usr/lib/.build-id/d6/3e63edfaf02c640d1e308bf8e30288cf3b646a
    modified-\&#8230;\&#8230;\&#8230;.T /usr/libexec/beesu
    modified-\&#8230;\&#8230;\&#8230;.T /usr/share/doc/beesu
    modified-\&#8230;\&#8230;\&#8230;.T /usr/share/licenses/beesu

The issue occurs because the changelog entry contains time \'in the
future\', i.e. later than when the original build happened. A
traditional changelog is used and the maintainer is working late at
night. In the local time, it is after midnight, so the date has already
changed, but the date in the UTC timezone hasn't changed yet. The
&#96;%changelog&#96; entries do not specify the timezone --- they are
implicitly in the UTC timezone. The maintainer erronously inserts a
&#96;%changelog&#96; entry with a timestamp that is one or more hours
ahead, and quickly pushes the changes and starts a build.

We use the timestamp of last changelog entry as the official \'time when
the build happens\', i.e. as source for &#96;\$SOURCE_DATE_EPOCH&#96;.
During the build, &#96;\$SOURCE_DATE_EPOCH&#96; is set, but it is set to
the future, so clamping of mtimes of files generated during the build is
ineffective. When we repeat the build, at least a few hours later, the
changelog timestamp is in the past, so clamping of mtimes to
&#96;\$SOURCE_DATE_EPOCH&#96; becomes effective again.

We end up with different timestamps on files that are generated during
the build.

From the spec file for &#96;beesu&#96;: &#8230;. \$ git show -U0
beesu.spec commit bb415496f28bf29c6a177be72cef5271c6e65af3 &#8230; Date:
Mon Jan 27 00:04:43 2025 +0100 &#8230; @@ -56,0 +59,3 @@ %changelog
+&#42; Mon Jan 27 2025 Name &lt;<address@example.com>&gt; - 2.7-50 +-
fix building of beesu in f42

\+ &#8230;.

As we can see from the commit timestamp, the time was Jan 27 00:04:43
+0100, which is Jan 26 23:04:43 UTC, and the timestamp in the
&#96;%changelog&#96; section is off-by-one.

# Solutions {#_solutions}

The easiest solution is to switch to
[rpmautospec](https://docs.pagure.org/fedora-infra.rpmautospec/). Then
the changelog timestamp is automatically generated from the commit
timestamp, which in turn is set automatically by &#96;git&#96;, so the
problem goes away.

Some alternative solutions are to either configure the tool used to
insert the changelog entry to use UTC, or to correct the timestamps by
hand.

Finally, consider &#42;&#42;not&#42;&#42; working so late at night. Open
source maintainers need to think about their long-term health too.

# Conference talks {#_conference_talks}

This page collects conference talks and other public presentations
around Fedora Reproducible Builds.

- \'[Reproducible builds in
  Fedora](https://www.youtube.com/watch?v=nJHh-VJnGt8)\' (Zbigniew
  Jędrzejewski-Szmek, Davide Cavalca) at [Flock to Fedora
  2024](https://cfp.fedoraproject.org/flock-2024/talk/SKWEXP/)

- \'[Making Fedora Linux (more)
  reproducible](https://www.youtube.com/watch?v=5c4gfXVPAbU)\' (Davide
  Cavalca) at [SCALE
  21x](https://www.socallinuxexpo.org/scale/21x/presentations/making-fedora-linux-more-reproducible)

- \'Reproducible builds in Fedora\' (Zbigniew Jędrzejewski-Szmek, not
  recorded) at [Jesień Linuksowa 2024](https://jesien.org/2024/)

- \'[Rewriting pyc files for fun and
  reproducibility](https://fosdem.org/2025/schedule/event/fosdem-2025-4072-rewriting-pyc-files-for-fun-and-reproducibility/)
  (Zbigniew Jędrzejewski-Szmek)\' at [FOSDEM
  2025](https://fosdem.org/2025/)
