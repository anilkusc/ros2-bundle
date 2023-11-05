
FROM gazebo:gzserver11
ARG WORLD_NAME
ENV WORLD_FILE=${WORLD_NAME}.sdf
WORKDIR /world
COPY . .
RUN chmod 777 entrypoint.sh
CMD ./entrypoint.sh