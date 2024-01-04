# **************************************main2

import cv2
import numpy as np
import pywt
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.conf import settings
import os

def embed_extract(host_image, watermark_image):
    try:
        print("Reading images...")
        host_image = cv2.imdecode(np.frombuffer(host_image.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
        watermark_image = cv2.imdecode(np.frombuffer(watermark_image.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
        print("Images read successfully.")
        # cv2.imshow("watermak_image", watermark_image)
        # cv2.imshow("host_image", host_image)
    except Exception as e:
        print(f"Error reading images: {e}")
        return HttpResponse(f"Error reading images: {e}")

    # Normalize the watermark images to the range [0, 1]
    watermark_image = watermark_image / 255.0

    # Apply DWT to the host image
    wavelet = 'haar'
    coeffs = pywt.dwt2(host_image, wavelet)
    LL, (LH, HL, HH) = coeffs

    # Define block size
    block_size = 8

    # Get the shape of the LH subband
    rows_dwt, cols_dwt = LH.shape

    # Calculate the number of blocks in each dimension
    num_blocks_rows = rows_dwt // block_size
    num_blocks_cols = cols_dwt // block_size
    variances = np.zeros((num_blocks_rows, num_blocks_cols))

    blocks = []
    for i in range(0, 256, 8):
        for j in range(0, 256, 8):
            block = HL[i:i + 8, j:j + 8]
            blocks.append(block)

    # Apply DCT to the watermark image
    watermark_dct = cv2.dct(watermark_image)

    rows, cols = watermark_dct.shape

    for i in range(rows):
        for j in range(cols - i, cols):
            watermark_dct[i, j] = 0

    num_blocks_rows_watermark = rows // block_size
    num_blocks_cols_watermark = cols // block_size

    for i in range(rows):
        for j in range(0, cols - i):
            LH[i, j] = watermark_dct[i, j]


    # Perform IDWT on the modified coefficients
    watermarked_image = pywt.idwt2(coeffs, wavelet)
    watermarked_image = watermarked_image / 255.0
    
    print("embedded successufully!")

    # Save the embedded watermark image
    watermarked_image_path = os.path.join(settings.MEDIA_ROOT, 'watermarked_image.png')
    cv2.imwrite(watermarked_image_path, watermarked_image * 255)

    # Return the URL of the embedded image
    watermarked_relative_path = os.path.relpath(watermarked_image_path, settings.MEDIA_ROOT)
    watermarked_image_url = os.path.join(settings.MEDIA_URL, watermarked_relative_path).replace("\\", "/")

    # Apply DWT to the watermarked image
    coeffs_w = pywt.dwt2(watermarked_image, wavelet)
    LL_w, (LH_w, HL_w, HH_w) = coeffs_w

    rows_hh,cols_hh = LH_w.shape
    extr_wt = np.zeros_like(LH_w)
    for i in range(0, 256):
        for j in range(256-i, 256):
            LH_w[i, j]=0

    # Extract the watermark from the HH subband
    extr = cv2.idct(LH_w)
    extr = extr * 255

    # Save the extracted watermark image
    extracted_image_path = os.path.join(settings.MEDIA_ROOT, 'extracted_watermark.png')
    cv2.imwrite(extracted_image_path, extr * 255)
    # cv2.imshow("extracted", extr)
    print("extracted successufully!")


    # Return the URL of the saved image
    extracted_relative_path = os.path.relpath(extracted_image_path, settings.MEDIA_ROOT)
    extracted_image_url = os.path.join(settings.MEDIA_URL, extracted_relative_path).replace("\\", "/")

    # Return both URLs
    return watermarked_image_url, extracted_image_url


def embed_extract_level2(host_image, watermark_image):
    try:
        print("Reading images...")
        host_image = cv2.imdecode(np.frombuffer(host_image.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
        watermark_image = cv2.imdecode(np.frombuffer(watermark_image.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
        print("Images read successfully.")
        # cv2.imshow("watermak_image", watermark_image)
        # cv2.imshow("host_image", host_image)
    except Exception as e:
        print(f"Error reading images: {e}")
        return HttpResponse(f"Error reading images: {e}")
    
    watermark_image = watermark_image / 255.0

    # Apply DWT to the host image
    wavelet = 'haar'
    coeffs = pywt.dwt2(host_image, wavelet)
    LL, (LH, HL, HH) = coeffs

    # cv2.imshow("HH 1st band", HH*255)

    # Get the shape of the LH subband
    rows_dwt, cols_dwt = HH.shape

    # Apply DCT to the watermark image
    watermark_dct = cv2.dct(watermark_image)
    # cv2.imshow('after dct',watermark_dct)

    rows, cols = watermark_dct.shape
    print(rows)
    for i in range(rows):
        for j in range(cols-i, cols):
            watermark_dct[i, j] = 0

    LL2, (LH2, HL2, HH2) = pywt.dwt2(HH, wavelet)
    # cv2.imshow("watermark dct",watermark_dct)
    # cv2.imshow("HH 2nd band", HH2)
    # embedding into hh band
    for i in range(rows):
        for j in range(0, cols-i):
            HH2[i,j]=watermark_dct[i, j]

    # Embed the watermark into the HH subband of the host image
    coeffs_2= (LL2, (LH2, HL2, HH2))
    # cv2.imshow("HH 2nd embedding", HH2)

    watermarked_hh= pywt.idwt2((LL2, (LH2, HL2, HH2)),wavelet)
    watermarked_image= pywt.idwt2((LL, (LH, HL, watermarked_hh)),wavelet)

    watermarked_image = watermarked_image/255 


    print("embedded successufully!")

    # Save the embedded watermark image
    watermarked_image_path = os.path.join(settings.MEDIA_ROOT, 'watermarked_image2.png')
    cv2.imwrite(watermarked_image_path, watermarked_image * 255)

    # Return the URL of the embedded image
    watermarked_relative_path = os.path.relpath(watermarked_image_path, settings.MEDIA_ROOT)
    watermarked_image_url = os.path.join(settings.MEDIA_URL, watermarked_relative_path).replace("\\", "/")

    # cv2.imshow("watermaked_image",cv2.resize(watermarked_image,(256,256)))

    #Apply DWT to the watermarked image
    coeffs_w = pywt.dwt2(watermarked_image, wavelet)
    LL_w, (LH_w, HL_w, HH_w) = coeffs_w

    LL2_w, (LH2_w, HL2_w, HH2_w) = pywt.dwt2(HH_w, wavelet)

    row_hh,cols_hh=HH2_w.shape
    extr_wt=np.zeros_like(HH2_w)
    for i in range(0, row_hh):
        for j in range(cols_hh-i,cols_hh):
            HH2_w[i, j]=0

    # cv2.imshow("HH extracting ",HH2_w*255)
    # Extract the watermark from the HH subband
    extr = cv2.idct(HH2_w)
    extr=extr*255

    # Save the extracted watermark image
    extracted_image_path = os.path.join(settings.MEDIA_ROOT, 'extracted_watermark2.png')
    cv2.imwrite(extracted_image_path, extr * 255)

    print("extracted successufully!")


    # Return the URL of the saved image
    extracted_relative_path = os.path.relpath(extracted_image_path, settings.MEDIA_ROOT)
    extracted_image_url = os.path.join(settings.MEDIA_URL, extracted_relative_path).replace("\\", "/")

    # Return both URLs
    return watermarked_image_url, extracted_image_url



def embed_extract_color(host_image, watermark_image):
    try:
        print("Reading images...")
        # host_image_ycc = cv2.imdecode(np.frombuffer(host_image.read(), np.uint8), cv2.COLOR_BGR2YCrCb)
        # watermark_image_ycc = cv2.imdecode(np.frombuffer(watermark_image.read(), np.uint8), cv2.COLOR_BGR2YCrCb)

        # Load the host image and the watermark image
        # host_image = cv2.imread('lenna.png')
        # watermark_image = cv2.imread('seagull.jpg')

        # Convert images to YCbCr color space
        host_image_ycc = cv2.cvtColor(host_image, cv2.COLOR_BGR2YCrCb)
        watermark_image_ycc = cv2.cvtColor(watermark_image, cv2.COLOR_BGR2YCrCb)


        # host_image = cv2.imdecode(np.frombuffer(host_image.read(), np.uint8))
        # watermark_image = cv2.imdecode(np.frombuffer(watermark_image.read(), np.uint8))
        print("Images read successfully.")

    except Exception as e:
        print(f"Error reading images: {e}")
        return HttpResponse(f"Error reading images: {e}") 

    # host_image_ycc = cv2.cvtColor(host_image, cv2.COLOR_BGR2YCrCb)
    # watermark_image_ycc = cv2.cvtColor(watermark_image, cv2.COLOR_BGR2YCrCb)

    # Extract the Y component
    host_image_y = host_image_ycc[:, :, 0]
    watermark_image_y = watermark_image_ycc[:, :, 0]  

    # Apply DWT to the Y component of the host image
    wavelet = 'haar'
    coeffs = pywt.dwt2(host_image_y, wavelet)
    LL, (LH, HL, HH) = coeffs

    # Define block size
    block_size = 8

    # Get the shape of the LH subband
    rows_dwt, cols_dwt = LH.shape
    # Calculate the number of blocks in each dimension
    num_blocks_rows = rows_dwt // block_size
    num_blocks_cols = cols_dwt // block_size

    # Initialize an array to store variances for each block
    # variances = np.zeros((num_blocks_rows, num_blocks_cols))

    # Apply DCT to the watermark image
    watermark_image_y_dct = cv2.dct(watermark_image_y/255)

    # Set the upper triangular part to zero
    rows, cols = watermark_image_y_dct.shape
    for i in range(rows):
        for j in range(cols - i, cols):
            watermark_image_y_dct[i, j] = 0

    # Embedding into HL subband
    for i in range(rows):
        for j in range(0, cols - i):
            LH[i, j] = watermark_image_y_dct[i, j]

    # Perform IDWT on the modified coefficients
    watermarked_image_y = pywt.idwt2((LL, (LH, HL, HH)), wavelet)

    watermarked_image_y = cv2.resize(watermarked_image_y, (host_image_y.shape[1], host_image_y.shape[0]))

    # Replace the Y component in the YCbCr image with the watermarked Y component
    watermarked_image_ycc = host_image.copy()
    watermarked_image_ycc[:, :, 0] = watermarked_image_y

    # Convert the watermarked YCbCr image back to BGR color space
    watermarked_image_ycc = cv2.cvtColor(watermarked_image_ycc,cv2.COLOR_YCrCb2BGR)


    print("embedded successufully!")

    # Save the embedded watermark image
    watermarked_image_path = os.path.join(settings.MEDIA_ROOT, 'watermarked_image3.png')
    cv2.imwrite(watermarked_image_path, watermarked_image_ycc * 255)

    # Return the URL of the embedded image
    watermarked_relative_path = os.path.relpath(watermarked_image_path, settings.MEDIA_ROOT)
    watermarked_image_url = os.path.join(settings.MEDIA_URL, watermarked_relative_path).replace("\\", "/")


    # Display the watermarked image
    # cv2.imshow("Watermarked Image", watermarked_image_ycc)
    # cv2.imwrite("watermarked_image_YCbCr_LH_lenna.jpg", watermarked_image_ycc)
    # Extract the watermark from the watermarked image
    coeffs_watermarked = pywt.dwt2(watermarked_image_y, wavelet)
    LL_w, (LH_w, HL_w, HH_w) = coeffs_watermarked
    # Set the upper triangular part to zero in the HL subband
    rows_hl, cols_hl = LH_w.shape
    for i in range(rows_hl):
        for j in range(cols_hl - i, cols_hl):
            LH_w[i, j] = 0
    if rows_hl % 2 != 0:
        LH_w = LH_w[:-1, :]
    # If the number of columns in HL_w is odd, remove the last column to make it even
    if cols_hl % 2 != 0:
        LH_w = LH_w[:, :-1]
    # Extract the watermark from the HL subband
    extracted_watermark_y = cv2.idct(LH_w)

    # Display the extracted watermark
    # cv2.imshow("Extracted Watermark", cv2.resize(extracted_watermark_y ,(256, 256)))
    # cv2.imwrite("extracted_watermar_hoo_YCbCr_lH.jpg", extracted_watermark_y*255)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Save the extracted watermark image
    extracted_image_path = os.path.join(settings.MEDIA_ROOT, 'extracted_watermark3.png')
    cv2.imwrite(extracted_image_path, extracted_watermark_y * 255)

    print("extracted successufully!")


    # Return the URL of the saved image
    extracted_relative_path = os.path.relpath(extracted_image_path, settings.MEDIA_ROOT)
    extracted_image_url = os.path.join(settings.MEDIA_URL, extracted_relative_path).replace("\\", "/")

    # Return both URLs
    return watermarked_image_url, extracted_image_url



# *************************************main2 end
