#!/usr/bin/env bash

VERSION=$1
MODE=$2

if [ "$VERSION" == "" ];then
    echo "please enter version"
elif [ "$MODE" == "" ]; then
    echo "please enter mode"
else

    if [ "$MODE" = "public" ];then
        PORT="33049"
    else
        PORT="13900"
    fi

    docker build -t ai-in-law/judgement:$VERSION-$MODE .

    docker stop $(docker ps -aq --filter name=judgement-[v0-9.]*-$MODE)
    docker rm $(docker ps -aq --filter name=judgement-[v0-9.]*-$MODE)

    docker run -d \
        --name judgement-$VERSION-$MODE \
        -p $PORT:8080 \
        --restart=always \
        --label=com.centurylinklabs.watchtower.enable=false \
        ai-in-law/judgement:$VERSION-$MODE
fi