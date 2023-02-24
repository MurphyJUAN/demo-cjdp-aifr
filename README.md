# nlp_judgement_frontend

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).



## Running on Docker Container

1. Build docker image with `docker build -t ai-in-law/judgement-frontend .`

2. Run container with

    - detach mode

        ```dockerfile
        docker run -d \
            --name ai-judgement-frontend-beta \
            -p 33049:8080 \
            --restart=always \
            ai-in-law/judgement-frontend
        ```

    - interactive mode

        ```dockerfile
        docker run -ti \
            --name ai-judgement-frontend-beta \
            -p 33049:8080 \
            --rm \
            ai-in-law/judgement-frontend \
            bash
        ```

        After run into the container's shell, you can see the default workdir is `/frontend`, then just excute `npm run dev`.

3. Open Web Browser and connected to <http://140.114.80.82:33049>

