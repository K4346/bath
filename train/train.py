from ultralytics import YOLO
println("start create model")
model = YOLO("yolov8n.pt")
println("start train model")
model.train(data="dataset/bath.yaml", epochs=3,device=0, project="results")
println("start export model")
model.export(format="onnx")
println("finish all")