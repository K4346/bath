TRAIN

docker build -t ultralytics-ubuntu ./train/Dokerfile

docker run -it -v "C:\Users\user\Desktop\NNforAnd\5bath\dataset":./dataset" -v "C:/Users/user/Desktop/NNforAnd/5bath/results":"/results" ultralytics-train

VALIDATE

docker build -t ultralytics-ubuntu ./val/Dockerfile

//dataset, results, modelPath
docker run -it -v "C:/Users/user/Desktop/NNforAnd/5bath/results":"/results" ultralytics-val -v "C:/Users/user/Desktop/NNforAnd/5bath/results/train/weights":"/model"


//docker run -it -v "C:\Users\user\Desktop\NNforAnd\5bath\dataset":./dataset" -v "C:/Users/user/Desktop/NNforAnd/5bath/results":"/results" ultralytics-val -v "C:/Users/user/Desktop/NNforAnd/5bath/results/train/weights":"/model"