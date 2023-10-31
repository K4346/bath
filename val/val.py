from ultralytics import YOLO
println("start model")
model = YOLO("./model/best.pt")
println("start val model")
model.val(project="results")
println("finish all")