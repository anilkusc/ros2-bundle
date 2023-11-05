
FROM gazebo:gzserver10
ARG WORLD_NAME
ENV WORLD_NAME=${WORLD_NAME}
WORKDIR /world
COPY . .
RUN chmod 777 entrypoint.sh
CMD ./entrypoint.sh