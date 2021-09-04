# Developed By Skay69

print(" - press 'q' key to change webcam, to close the program just type 'q' until all webcam close -")
try:
	for i in range(5):
		vid = cv2.VideoCapture(i, cv2.CAP_DSHOW)
		while True:
			ret, frame = vid.read()
			cv2.imshow('PY-WEBCAM', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		vid.release()
		cv2.destroyAllWindows()
except:
	pass
