# Site
the simple site: http://cklin.top

# Formed
The Project is about the BaiduZhidao's Crawler. Theere are five Docker Service:
1. db: only about the MySQL
2. backend: Django(Raw Data, provide the data API processed by pandas in advance) + DRF(Json-format Data)
3. frontend: contains the Vue(Nuxt(highcharts)) Data-Visual. (Due to the limit of Github'size, I drop the node_modules DIR) 
4. Crawler: Scrapy+Scrapyd (Spider simple start and stop by Django)
5. Sanic: the Tensorflow Model + predict result(by pre-trained model) + return result API by Sanic router(view)

# Deployment
1 docker-compose.yaml + 5 Dockerfile

# Run Command
first, start all services.
    docker-compose up -d 
second, send the spider code to the scrapyd(also in docker)
    docker-compose exec crawl  scrapyd-deploy Cython_lin -p Baidu
  
# Notice
Because the github platform is support 100MB (max)  
But MyCode is 1.2 GB (include data and Model)  
Im sorry that I cant commit the total code.  
But you can learn the the project's structure of the docker&docker-compose service.

