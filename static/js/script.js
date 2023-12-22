let item_form = document.querySelector('#buy-item-form').addEventListener('submit', function () {
    const item_btn = document.getElementById('buy-item-id')
    const csrftoken = Cookies.get('csrftoken');
    let stripe = Stripe("pk_test_51OPQXAD7OM3xNb3XUZoHMtcolzzo1ZtHhO9m6WXc0G2kKRFBCl5x7kwuHg3fIFdagwYqoOaQZOZjX3LLyYkfMgsf00PLp6P0U4");

    fetch(`/buy/${item_btn.value}/`, {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken }
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (session) {
            return stripe.redirectToCheckout({ sessionId: session.sessionId })
        })
        .then(function (result) {
            if (result.error) {
                alert(result.error.message);
            }
        })



})

