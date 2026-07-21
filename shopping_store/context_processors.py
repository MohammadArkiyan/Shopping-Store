def page_contact(request):
    context = {
        # ************ this is footer data ************
        'site_name': '',
        'footer_text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do'
                       ' eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut'
                       ' enim ad minim veniam, quis nostrud exercitation ullamco laboris ',

        # fashion images
        'men_fashions': 'static/img/men-fashions.png',
        'women_fashions': 'static/img/women-fashions.png',
        'kids_fashions': 'static/img/kids-fashions.png',

        # offer images
        'offer1_image': 'static/img/offer-1.png',
        'offer2_image': 'static/img/offer-2.jpg',

        # contact data.
        'email': 'mohammadarkiyan30@gmail.com',
        'phone_number': '09339804252',
        'customer_service_number': '012 23233434',
        'location': '123 Street, Rasht, IRAN',
        'instagram': '',
        'facebook': '',
        'x': '',
        'linkedin': '',

        # Company image urls.
        'company_name_image1': 'static/img/Artboard 1.png',
        'company_name_image2': 'static/img/Artboard 2.png',
        'company_name_image3': 'static/img/Artboard 3.png',
        'company_name_image4': 'static/img/Artboard 4.png',
        'company_name_image5': 'static/img/Artboard 5.png',
        'company_name_image6': 'static/img/Artboard 6.png',
        'company_name_image7': 'static/img/Artboard 7.png',
        'company_name_image8': 'static/img/Artboard 8.png',


    }
    return context
