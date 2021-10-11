var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
// Setup Stripe
var stripe = Stripe(stripe_public_key);
// Create instance of Stripe elements
var elements = stripe.elements();
// Below styles for card element come from Stripe documentation
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#e71d36',
        iconColor: '#e71d36'
    }
};
// Create a card element
var card = elements.create('card', {style: style});
card.mount('#card-element')




