import os
from ruamel import yaml

# 添加需要处理文件的路径
path = "D:\Git\GitHub\pytools-yaml\TestDir"

# 编辑MySQL相关配置
mysql_ip="129.3.33.9897"

# 编辑Redis相关配置
redis_host="3.3.1.23"
redis_port="3434"
redis_password="vova_is_good"

# 编辑ES相关配置
es_ip = "4.13.33.3:333"

# 编辑注册中心
eureka_ip="http://120.0.0.33:9292/eureka/"


# 是否創建新yml文件
createNewFile = 0



def findYml(path):
    print("path === "+path)
    for root, dirs, files in os.walk(path):
        print("file=================")
        for file in files:
            file_path = os.path.join(root,file)
            print("发现yml文件 =====> 路径 = " + file_path + "\n")
            changeYml(file_path)



def changeYml(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        ymlDoc = yaml.round_trip_load(f)
        # print(type(ymlDoc))

        if "spring" in ymlDoc.keys():
            # dealwith MySQL
            if "datasource" in ymlDoc["spring"].keys() and "url" in ymlDoc["spring"]["datasource"].keys():
                print("MySQL-----------修改前value="+ymlDoc["spring"]["datasource"]["url"])

                mysqlUrl=str(ymlDoc["spring"]["datasource"]["url"]);
                p1 = mysqlUrl.index('mysql://')
                p2 = mysqlUrl.index(':3306')
                ip = mysqlUrl[p1+8:p2]

                ymlDoc["spring"]["datasource"]["url"]=mysqlUrl.replace(ip, mysql_ip)
                print("MySQL-----------修改后value=" + ymlDoc["spring"]["datasource"]["url"]+"\n")
            # dealwith Redis
            if "redis" in ymlDoc["spring"].keys():
                if "host" in ymlDoc["spring"]["redis"].keys():
                    print("RedisHost-----------修改前value=" + ymlDoc["spring"]["redis"]["host"])
                    ymlDoc["spring"]["redis"]["host"] = redis_host
                    print("RedisHost-----------修改后value=" + ymlDoc["spring"]["redis"]["host"] + "\n")

                if "port" in ymlDoc["spring"]["redis"].keys():
                    print("RedisPort-----------修改前value=" + ymlDoc["spring"]["redis"]["port"])
                    ymlDoc["spring"]["redis"]["port"] = redis_port
                    print("RedisPort-----------修改后value=" + ymlDoc["spring"]["redis"]["port"] + "\n")

                if "password" in ymlDoc["spring"]["redis"].keys():
                    print("RedisPassword-----------修改前value=" + ymlDoc["spring"]["redis"]["password"])
                    ymlDoc["spring"]["redis"]["password"] = redis_password
                    print("RedisPassword-----------修改后value=" + ymlDoc["spring"]["redis"]["password"]+ "\n")
            # dealwith ES
            if "data" in ymlDoc["spring"].keys():
                if "elasticsearch" in ymlDoc["spring"]["data"].keys() and "cluster-nodes" in ymlDoc["spring"]["data"]["elasticsearch"].keys():
                    print("Elasticsearch-----------修改前value=" + ymlDoc["spring"]["data"]["elasticsearch"]["cluster-nodes"])
                    ymlDoc["spring"]["data"]["elasticsearch"]["cluster-nodes"] = es_ip
                    print("Elasticsearch-----------修改后value=" + ymlDoc["spring"]["data"]["elasticsearch"]["cluster-nodes"]+"\n")

        if "eureka" in ymlDoc.keys():
            # dealwith MySQL
            if "client" in ymlDoc["eureka"].keys() \
                    and "service-url" in ymlDoc["eureka"]["client"].keys()\
                    and "defaultZone" in ymlDoc["eureka"]["client"]["service-url"].keys():
                abd=ymlDoc["eureka"]["client"]["service-url"]["defaultZone"]
                print("Eureka-----------修改前value=" + abd)
                ymlDoc["eureka"]["client"]["service-url"]["defaultZone"] = eureka_ip
                print("Eureka-----------修改后value=" + ymlDoc["eureka"]["client"]["service-url"]["defaultZone"]+"\n")

        if createNewFile ==1 :
            with open(file_path.split('.')[0]+"-new.yml", 'w', encoding='utf-8') as w_f:
                yaml.round_trip_dump(ymlDoc, w_f)
        else:
            with open(file_path, 'w', encoding='utf-8') as w_f:
                yaml.round_trip_dump(ymlDoc, w_f)
        ymlDoc = 0

findYml(path)