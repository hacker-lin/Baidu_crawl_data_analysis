FROM node:10.15.3
RUN mkdir -p /usr/src/app
ENV HOME=/usr/src/app
WORKDIR $HOME
COPY . $HOME
WORKDIR $HOME/nuxt
RUN rm -rf node_modules
#RUN rm -rf package lock.json
#RUN npm cache clear --force

RUN npm install 
RUN npm build
