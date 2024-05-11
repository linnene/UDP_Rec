import socket
import numpy as np
import cv2

# 设置socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 5094))  # 绑定监听的IP地址和端口号

try:
    while True:
        data, addr = sock.recvfrom(65507)  # 接收大数据包
        if not data:
            print("无数据，结束")
            break
        nparr = np.frombuffer(data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is not None:
            cv2.imshow('Video Stream', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # 按q退出
                break
finally:
    sock.close()
    cv2.destroyAllWindows()
