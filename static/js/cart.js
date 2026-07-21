
// online

/* document.addEventListener('DOMContentLoaded', function() {


    // --- Cart AJAX Updates (Add to Cart & Update Quantity) ---
    const allButtons = document.querySelectorAll('.cart-update-btn, .add-to-cart-btn');

    allButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            // Only prevent default for cart-update-btn or if specifically needed
            // If the theme handles the click for Detail page, we don't want to break it.

            let url = '';
            let productId = this.dataset.productId;
            let isRemoveBtn = this.classList.contains('btn-danger') || this.querySelector('.fa-times');

            let fetchOptions = {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json',
                }
            };

            // Case A: Update/Remove items in the Cart Page
            if (this.classList.contains('cart-update-btn')) {
                event.preventDefault();
                url = this.getAttribute('href');
                fetchOptions.method = 'GET';
            }
            // Case B: Add item to cart from Product Detail Page
            else if (this.classList.contains('add-to-cart-btn')) {
                event.preventDefault();
                const form = this.closest('form');
                if (productId && form) {
                    url = '/cart/add/' + productId + '/';
                    const formData = new FormData(form);
                    fetchOptions.method = 'POST';
                    fetchOptions.body = formData;

                    // Note: Ensure your form includes the {% csrf_token %}
                }
            }

            if (url) {
                fetch(url, fetchOptions)
                .then(response => response.json())
                .then(data => {
                    if (data.ok) {
                        // 1. Update Cart Badge in Header
                        const cartBadge = document.getElementById('cart-total-qty');
                        if (cartBadge) {
                            cartBadge.innerText = data.total_qty;
                        }

                        // 2. Success Feedback
                        if (this.classList.contains('add-to-cart-btn')) {
                            alert('Product added to cart!');
                        }

                        // 3. Update Cart Totals (Price/Subtotal)
                        const subtotalElem = document.getElementById('cart-subtotal');
                        const finalTotalElem = document.getElementById('cart-final-total');

                        if (subtotalElem) subtotalElem.innerText = data.subtotal;
                        if (finalTotalElem) finalTotalElem.innerText = data.final_total;

                        // 4. Update UI Rows for Cart Page
                        if (productId) {
                            if (data.item === null || data.item.quantity <= 0 || isRemoveBtn) {
                                let row = document.getElementById('row-' + productId);
                                if (row) row.remove();
                            } else if (data.item) {
                                let qtyInput = document.getElementById('qty-' + productId);
                                if (qtyInput) qtyInput.value = data.item.quantity;

                                let lineTotal = document.getElementById('total-' + productId);
                                if (lineTotal) lineTotal.innerText = data.item.line_total;
                            }
                        }
                    }
                })
                .catch(err => {
                    console.error('Fetch Error:', err);
                    alert('An error occurred. Please try again.');
                });
            }
        });
    });
}); */



document.addEventListener('DOMContentLoaded', function() {

    // --- Cart AJAX Updates (Add to Cart & Update Quantity) ---
    const allButtons = document.querySelectorAll('.cart-update-btn, .add-to-cart-btn');

    allButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            // Only prevent default for cart-update-btn or if specifically needed
            // If the theme handles the click for Detail page, we don't want to break it.

            let url = '';
            let productId = this.dataset.productId;
            let isRemoveBtn = this.classList.contains('btn-danger') || this.querySelector('.fa-times');

            let fetchOptions = {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json',
                }
            };

            // Case A: Update/Remove items in the Cart Page
            if (this.classList.contains('cart-update-btn')) {
                event.preventDefault();
                url = this.getAttribute('href');
                fetchOptions.method = 'GET';
            }
            // Case B: Add item to cart from Product Detail Page
            else if (this.classList.contains('add-to-cart-btn')) {
                event.preventDefault();
                const form = this.closest('form');
                if (productId && form) {
                    url = '/cart/add/' + productId + '/';
                    const formData = new FormData(form);
                    fetchOptions.method = 'POST';
                    fetchOptions.body = formData;

                    // Note: Ensure your form includes the {% csrf_token %}
                }
            }

            if (url) {
                fetch(url, fetchOptions)
                .then(response => response.json())
                .then(data => {
                    if (data.ok) {
                        // 1. Update Cart Badge in Header
                        const cartBadge = document.getElementById('cart-total-qty');
                        if (cartBadge) {
                            cartBadge.innerText = data.total_qty;
                            localStorage.setItem('cartQty', data.total_qty); // Store cart quantity in localStorage
                        }

                        // 2. Success Feedback
                        if (this.classList.contains('add-to-cart-btn')) {
                            alert('Product added to cart!');
                        }

                        // 3. Update Cart Totals (Price/Subtotal)
                        const subtotalElem = document.getElementById('cart-subtotal');
                        const finalTotalElem = document.getElementById('cart-final-total');
                        if (subtotalElem) subtotalElem.innerText = data.subtotal;
                        if (finalTotalElem) finalTotalElem.innerText = data.final_total;

                        // 4. Update UI Rows for Cart Page
                        if (productId) {
                            if (data.item === null || data.item.quantity <= 0 || isRemoveBtn) {
                                let row = document.getElementById('row-' + productId);
                                if (row) row.remove();
                            } else if (data.item) {
                                let qtyInput = document.getElementById('qty-' + productId);
                                if (qtyInput) qtyInput.value = data.item.quantity;
                                let lineTotal = document.getElementById('total-' + productId);
                                if (lineTotal) lineTotal.innerText = data.item.line_total;
                            }
                        }
                    }
                })
                .catch(err => {
                    console.error('Fetch Error:', err);
                    alert('An error occurred. Please try again.');
                });
            }
        });
    });

    // Retrieve cart quantity from localStorage on page load
    const storedQty = localStorage.getItem('cartQty');
    if (storedQty) {
        const cartBadge = document.getElementById('cart-total-qty');
        if (cartBadge) {
            cartBadge.innerText = storedQty;
        }
    }
});
