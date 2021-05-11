import cv2
import peopledb
import people
peopleDB = peopledb.PeopleDB()


def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def getFaceToTrain():
    # Bước 1: Tấm ảnh và tệp tin xml
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    image = cv2.imread("a.jpg")
    cam = cv2.VideoCapture(0)

    id = input('enter your id: ')
    name = input('enter your name: ')
    age = input('enter your age: ')
    gender = input('enter your gender: ')
    peopleDB.add(people.People(id, name, gender, age))
    sampleNum = 0
    while(True):
        ret, img = cam.read()
        # img = image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # incrementing sample number
            sampleNum = sampleNum+1
            # saving the captured face in the dataset folder
            cv2.imwrite("dataSet/User."+str(id) + '.' +
                        str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])

        # wait for 100 miliseconds
        cv2.imshow('frame', img)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is morethan 20
        elif sampleNum > 200:
            break
    cam.release()
    cv2.destroyAllWindows()


getFaceToTrain()
