# import cv2
# from django.shortcuts import render
# from django.http import HttpResponse
# import numpy as np
# from .utils import embed_extract

# def home(request):
#     return render(request, 'watermark/home.html')

# def embed(request):
#     if request.method == 'POST' and 'embed' in request.POST:
#         host_image = request.FILES['host_image']
#         watermark_image = request.FILES['watermark_image']

#         # Save uploaded images
#         host_image_path = 'images/' + host_image.name
#         watermark_image_path = 'images/' + watermark_image.name
#         with open(host_image_path, 'wb') as f:
#             f.write(host_image.read())
#         with open(watermark_image_path, 'wb') as f:
#             f.write(watermark_image.read())

#         # Embed watermark
#         abc, coeffs = embed_watermark(host_image_path, watermark_image_path)
        

#         # Display the watermarked image in the template
#         watermarked_image_path = 'images/watermarked_image.png'
#         # watermarked_image_path = 'watermark\static\images\watermarked_image.png'

#         extract_watermark(watermarked_image_path, coeffs)

#         return render(request, 'watermark/embed.html', {'result': 'Embedded successfully!', 'watermarked_image_path': watermarked_image_path})

#     return render(request, 'watermark/home.html')





# def home(request):
#     return render(request, 'watermark/home.html')

# def embed(request):
#     if request.method == 'POST' and 'embed' in request.POST:
#         host_image = request.FILES['host_image']
#         watermark_image = request.FILES['watermark_image']

#         # Save uploaded images
#         host_image_path = 'images/' + host_image.name
#         watermark_image_path = 'images/' + watermark_image.name
#         with open(host_image_path, 'wb') as f:
#             f.write(host_image.read())
#         with open(watermark_image_path, 'wb') as f:
#             f.write(watermark_image.read())

#         # Embed and extract watermark
#         watermarked_image_path, extracted_watermark_path = embed_extract(host_image_path, watermark_image_path)

#         return render(request, 'watermark/embed.html', {'result': 'Embedded successfully!', 'watermarked_image_path': watermarked_image_path, 'extracted_watermark_path': extracted_watermark_path})

#     return render(request, 'watermark/home.html')





# watermark/views.py
# from django.shortcuts import render
# from .utils import embed_watermark, extract_watermark

# def embed(request):
#     if request.method == 'POST':
#         # Assuming you have a form with file inputs for host_image and watermark_image
#         host_image = request.FILES['lenna.png'].read()
#         watermark_image = request.FILES['seagull.jpg'].read()


#         # Save the images to temporary files (adjust as needed)
#         host_image_path = 'images\lenna.png'
#         watermark_image_path = 'images\seagull.jpg'

#         with open(host_image_path, 'wb') as host_file:
#             host_file.write(host_image)

#         with open(watermark_image_path, 'wb') as watermark_file:
#             watermark_file.write(watermark_image)

#         # Call the embed_watermark function
#         embed_watermark(host_image_path, watermark_image_path)

#         # Optionally, you can return a response or render a template
#         return render(request, 'watermark/embed.html')

#     return render(request, 'watermark/embed.html')

# def extract(request):
#     if request.method == 'POST':
#         # Assuming you have a form with a file input for the watermarked_image
#         watermarked_image = request.FILES['watermarked_image'].read()

#         # Save the watermarked image to a temporary file (adjust as needed)
#         watermarked_image_path = 'path/to/temp/watermarked_image.png'

#         with open(watermarked_image_path, 'wb') as watermarked_file:
#             watermarked_file.write(watermarked_image)

#         # Call the extract_watermark function
#         extracted_watermark = extract_watermark(watermarked_image_path)

#         # Optionally, you can return a response or render a template
#         return render(request, 'watermark_app/extract.html', {'extracted_watermark': extracted_watermark})

#     return render(request, 'watermark_app/extract.html')





# main*****************************************
# watermark_project/watermark/views.py
# from django.shortcuts import render
# from django.http import HttpResponse
# from .utils import embed_extract

# def index(request):
#     return render(request, 'watermark/index.html')

# def embed_extract(request):
#     if request.method == 'POST':
#         host_image = request.FILES['host_image']
#         watermark_image = request.FILES['watermark_image']
#         # watermarked_image = request.FILES.get('watermarked_image', None)

#         result_image = embed_extract(host_image, watermark_image)
#         return render(request, 'watermark/index.html', {'result_image': result_image})
#     return HttpResponse("Invalid request method")



# def embed_extract_view(request):
#     if request.method == 'POST':
#         host_image = request.FILES['host_image']
#         watermark_image = request.FILES['watermark_image']

#         result_image = embed_extract(host_image, watermark_image)
#         return render(request, 'watermark/index.html', {'result_image': result_image})
#     return HttpResponse("Invalid request method")


# ******************************************Submain
# def embed_extract_view(request):
#     if request.method == 'POST':
#         host_image_file = request.FILES['host_image']
#         watermark_image_file = request.FILES['watermark_image']

#         # Read the content of the uploaded files
#         host_image_content = host_image_file.read()
#         watermark_image_content = watermark_image_file.read()

#         # Convert the content to numpy arrays
#         host_image = cv2.imdecode(np.frombuffer(host_image_content, np.uint8), cv2.IMREAD_GRAYSCALE)
#         watermark_image = cv2.imdecode(np.frombuffer(watermark_image_content, np.uint8), cv2.IMREAD_GRAYSCALE)

#         # Perform watermark embedding and extraction
#         extracted_image_url = embed_extract(host_image, watermark_image)

#         if isinstance(extracted_image_url, HttpResponse):
#             # If the result is an HttpResponse, something went wrong
#             return extracted_image_url
#         else:
#             # If the result is an image or any other data, handle it as needed
#             return render(request, 'watermark/home.html', {'extracted_image_url': extracted_image_url})

#     return HttpResponse("Invalid request method")

# ***************************************



# ***********************************main2

# from django.shortcuts import render
# from django.http import HttpResponse
# from .utils import embed_extract

# def index(request):
#     return render(request, 'watermark/index.html')

# def embed_extract_view(request):
#     if request.method == 'POST':
#         host_image_file = request.FILES['host_image']
#         watermark_image_file = request.FILES['watermark_image']

#         # Perform watermark embedding and extraction
#         result_image = embed_extract(host_image_file, watermark_image_file)

#         if isinstance(result_image, HttpResponse):
#             # If the result is an HttpResponse, something went wrong
#             return result_image
#         else:
#             return render(request, 'watermark/index.html', {'result_image': result_image})

#     return HttpResponse("Invalid request method")


# *************************************




# ***************************************main3

# views.py

# from django.shortcuts import render
# from django.http import HttpResponse
# from .utils import embed_extract
# import cv2
# import numpy as np

# def home(request):
#     return render(request, 'watermark/home.html')

# def index(request):
#     return render(request, 'watermark/index.html')

# def embed_extract_view(request):
#     if request.method == 'POST':
#         host_image_file = request.FILES['host_image']
#         watermark_image_file = request.FILES['watermark_image']

#         # Perform watermark embedding and extraction
#         watermarked_image_url, extracted_image_url = embed_extract(host_image_file, watermark_image_file)

#         if isinstance(watermarked_image_url, HttpResponse):
#             # If there's an error, return the error response
#             return watermarked_image_url

#         return render(request, 'watermark/index.html', {'watermarked_image_url': watermarked_image_url, 'extracted_image_url': extracted_image_url})

#     return HttpResponse("Invalid request method")


# ******************************************main3 end



# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import embed_extract, embed_extract_level2, embed_extract_color

def home(request):
    return render(request, 'watermark/home.html')

def index(request):
    return render(request, 'watermark/index.html')

def index1(request):
    return render(request, 'watermark/index1.html')

def color1(request):
    return render(request, 'watermark/color1.html')

def embed_extract_view(request):
    if request.method == 'POST':
        host_image_file = request.FILES.get('host_image')
        watermark_image_file = request.FILES.get('watermark_image')

        if not host_image_file or not watermark_image_file:
            return HttpResponse("Invalid form submission. Please provide both host and watermark images.")

        # Perform watermark embedding and extraction
        watermarked_image_url, extracted_image_url = embed_extract(host_image_file, watermark_image_file)

        if isinstance(watermarked_image_url, HttpResponse):
            # If there's an error, return the error response
            return watermarked_image_url

        # If successful, you can redirect back to the home or index page
        # return redirect('index')  # Change 'home' to 'index' if you prefer redirecting to the 'index' page
        return render(request, 'watermark/index.html', {'watermarked_image_url': watermarked_image_url, 'extracted_image_url': extracted_image_url})
    
    return HttpResponse("Invalid request method")

def embed_extract_level2_view(request):
    if request.method == 'POST':
        host_image_file = request.FILES.get('host_image')
        watermark_image_file = request.FILES.get('watermark_image')

        if not host_image_file or not watermark_image_file:
            return HttpResponse("Invalid form submission. Please provide both host and watermark images.")

        # Perform watermark embedding and extraction
        watermarked_image_url, extracted_image_url = embed_extract_level2(host_image_file, watermark_image_file)

        if isinstance(watermarked_image_url, HttpResponse):
            # If there's an error, return the error response
            return watermarked_image_url

        # If successful, you can redirect back to the home or index page
        # return redirect('index')  # Change 'home' to 'index' if you prefer redirecting to the 'index' page
        return render(request, 'watermark/index1.html', {'watermarked_image_url': watermarked_image_url, 'extracted_image_url': extracted_image_url})
    
    return HttpResponse("Invalid request method")

# def embed_extract_color_view(request):
#     if request.method == 'POST':
#         host_image_file = request.FILES.get('host_image')
#         watermark_image_file = request.FILES.get('watermark_image')

#         if not host_image_file or not watermark_image_file:
#             return HttpResponse("Invalid form submission. Please provide both host and watermark images.")

#         # Perform watermark embedding and extraction
#         watermarked_image_url, extracted_image_url = embed_extract_color(host_image_file, watermark_image_file)

#         if isinstance(watermarked_image_url, HttpResponse):
#             # If there's an error, return the error response
#             return watermarked_image_url

#         # If successful, you can redirect back to the home or index page
#         # return redirect('index')  # Change 'home' to 'index' if you prefer redirecting to the 'index' page
#         return render(request, 'watermark/color1.html', {'watermarked_image_url': watermarked_image_url, 'extracted_image_url': extracted_image_url})
    
#     return HttpResponse("Invalid request method")


def embed_extract_color_view(request):
    if request.method == 'POST':
        host_image_file = request.FILES.get('host_image')
        watermark_image_file = request.FILES.get('watermark_image')

        if not host_image_file or not watermark_image_file:
            return HttpResponse("Invalid form submission. Please provide both host and watermark images.")

        # Perform watermark embedding and extraction
        result = embed_extract_color(host_image_file, watermark_image_file)

        if isinstance(result, HttpResponse):
            # If there's an error, return the error response
            return result

        # If successful, unpack the result tuple
        watermarked_image_url, extracted_image_url = result

        # If successful, you can redirect back to the home or index page
        # return redirect('index')  # Change 'home' to 'index' if you prefer redirecting to the 'index' page
        return render(request, 'watermark/color1.html', {'watermarked_image_url': watermarked_image_url, 'extracted_image_url': extracted_image_url})
    
    return HttpResponse("Invalid request method")
