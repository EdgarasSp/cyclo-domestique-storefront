$(document).ready(function() {
    
    // Disable +/- buttons outside 1-99 range
    function handleEnableDisable(itemId, itemAmount) {

        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        console.log(currentValue)
        var maxValue = parseInt($(`.max_${itemAmount}`).val());
        console.log(maxValue)
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > maxValue;
        console.log(plusDisabled)
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
    });

    // Decrement quantity
    $('.decrement-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
    });
});