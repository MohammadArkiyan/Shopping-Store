$(document).ready(function() {

    const searchInput = $('#live-search-input');
    const resultsContainer = $('#search-results-container');
    const searchUrl = searchInput.data('url') || '/search-endpoint';
    let typingTimer;

    searchInput.on('keyup', function() {
        const query = $(this).val().trim();

        clearTimeout(typingTimer);

        if (query.length < 2) {
            resultsContainer.hide().empty();
            return;
        }


        typingTimer = setTimeout(function() {
            sendSearchRequest(query);
        }, 500);
    });

    function sendSearchRequest(query) {

        resultsContainer.html('<div class="p-3 text-muted">Searching...</div>').show();

        $.ajax({
            url: searchUrl,
            method: 'GET',
            data: { 'q': query },
            dataType: 'json',

            success: function(response) {
                console.log("Server Response:", response);


                let products = [];
                if (response.results && Array.isArray(response.results)) {
                    products = response.results;
                } else if (Array.isArray(response)) {
                    products = response;
                }

                renderResults(products);
            },

            error: function(xhr, status, error) {
                console.error("Search Error:", error);
                resultsContainer.html('<div class="p-3 text-danger">Error loading results.</div>');
            }
        });
    }

    function renderResults(products) {
        resultsContainer.empty();

        if (!products || products.length === 0) {
            resultsContainer.html('<div class="p-3 text-muted">No results found.</div>');
        } else {
            products.forEach(product => {

                const imgUrl = product.image_url ? product.image_url : 'https://via.placeholder.com/50';

                const itemHtml = `
                    <a href="${product.url}" class="d-flex align-items-center p-2 border-bottom text-decoration-none text-dark hover-bg" style="display: flex; align-items: center; padding: 10px; border-bottom: 1px solid #eee; text-decoration: none; color: #333;">
                        <img src="${imgUrl}" style="width: 50px; height: 50px; object-fit: cover; margin-right: 10px; border-radius: 4px;">
                        <div>
                            <h6 class="m-0" style="font-size: 14px; margin: 0; font-weight: bold;">${product.name}</h6>
                             ${product.price ? `<small class="text-muted">${product.price}</small>` : ''}
                        </div>
                    </a>
                `;
                resultsContainer.append(itemHtml);
            });
        }

        resultsContainer.show();
    }


    $(document).on('click', function(e) {
        if (!$(e.target).closest('#search-form').length) {
            resultsContainer.hide();
        }
    });
});