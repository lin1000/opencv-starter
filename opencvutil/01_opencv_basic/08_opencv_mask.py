
        # ###
        # print im.shape
        # print type(im)
        # im1 = cv2.cvtColor( im, cv2.COLOR_BGR2GRAY)
        # ret, mask = cv2.threshold(im1, 120, 255, cv2.THRESH_BINARY)
        # im1_mask = cv2.bitwise_and(im1,im1,mask = mask)
        # cv2.imwrite(os.path.join(path_to_output_folder, str(right)+'mask.png'),mask)
        # cv2.imwrite(os.path.join(path_to_output_folder, "test1"+ str(right)+'.png'),im1)
        # cv2.imwrite(os.path.join(path_to_output_folder, "test1"+ str(right)+'mask.png'),im1_mask)
        # im2_g = im[:,:,0] #channel from 3->1
        # im2_r = im[:,:,1] #channel from 3->1
        # im2_b = im[:,:,2] #channel from 3->1
        # if(np.all(im2_g==im2_r) and np.all(im2_g==im2_b)):
        #     print("Grayscaled Image")   
        # else:
        #     print("BRG Image")
        # print("im2.g",im2_g)
        # print("im2.r",im2_r)
        # print("im2.b",im2_b)
        # cv2.imwrite(os.path.join(path_to_output_folder, "test2"+ str(right)+'.png'),im2)
        # im3 = im.set(mask,cv2.Scalar(120,120,255))
        # cv2.imwrite(os.path.join(path_to_output_folder, "test3"+ str(right)+'.png'),im3)
        # ###