import cv2


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    img = cv2.imread('lena.jpg', 1)
    print(img)

    cv2.imshow('image', img)

    k = cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('lena_copy.png', img)
        cv2.destroyAllWindows()