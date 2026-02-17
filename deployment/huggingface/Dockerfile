FROM fedora:43

EXPOSE 7860

RUN dnf install python3.13 uv git-core -y

RUN useradd -m -u 1000 user
RUN mkdir -p /app && chown -R user:user /app

RUN git clone --depth 1 https://github.com/NeuroML/neuroml-ai.git /app
RUN chown -R user:user /app

WORKDIR /app
USER user

RUN uv venv /app/nml-ai-venv
ENV VIRTUAL_ENV=/app/nml-ai-venv
ENV PATH="/app/nml-ai-venv/bin:$PATH"

RUN pwd
RUN ls -lash
RUN uv pip install -r requirements.txt

# in huggingface folder
COPY --chown=user scripts/* /app/scripts/
RUN chmod +x scripts/docker-deploy.sh

ENV GEN_RAG_CHAT_MODEL="huggingface:Qwen/Qwen3-4B-Instruct-2507:cheapest"
ENV GEN_RAG_VS_CONFIG="/app/scripts/vector-stores.json"
ENV RUNNING_IN_DOCKER=1

CMD ["./scripts/docker-deploy.sh"]
