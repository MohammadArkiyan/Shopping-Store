document.addEventListener('DOMContentLoaded', function() {


    const ajaxFilterForm = document.getElementById('ajaxFilterForm');
    const ajaxCheckboxes = document.querySelectorAll('.ajax-filter-checkbox');

    const productContainer = document.querySelector('.col-lg-9.col-md-8');

    if (!ajaxFilterForm || !productContainer) {

        return;
    }

    const shopBaseUrl = ajaxFilterForm.dataset.shopUrl;
    if (!shopBaseUrl) {
        console.error("Shop URL is missing from the AJAX filter form data attribute.");
        return;
    }


    function applyAjaxFilter() {


        const params = new URLSearchParams();

        ajaxCheckboxes.forEach(checkbox => {
            if (checkbox.checked) {

                params.append(checkbox.name, checkbox.value);
            }
        });


        const url = shopBaseUrl + '?' + params.toString();


        fetch(url, {
            method: 'GET',
            headers: {

                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
             if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(html => {




            productContainer.innerHTML = html;


            window.history.pushState(null, '', url);
        })
        .catch(error => console.error('Error applying AJAX filter:', error));
    }


    ajaxCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', applyAjaxFilter);
    });


    window.addEventListener('popstate', function(event) {

        window.location.reload();
    });
});