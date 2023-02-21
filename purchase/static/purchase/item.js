document.addEventListener('DOMContentLoaded', function() {
    //click по кнопке оплата заказа
    document.querySelector('#openorder').addEventListener('click', open_item);

    //click по любой из ссылок
    document.querySelectorAll('.openitem').forEach(function(link){link.addEventListener('click', open_item)})

    //click по checkout
    document.getElementById('checkout-button').addEventListener('click', buy_item);
    
    //меняем количество товаров в заказе
    document.querySelectorAll('.qntchanger').forEach(function(button){button.addEventListener('click', itemqnt);})

    // По умолчанию показываем страницу с товарами и заказом
    all_items();  

})


function itemqnt() {
    const td = this.parentElement;
    const tr = td.parentElement;              //нашли родительскую строку таблицы
    let counter = tr.querySelector('.counter')
    const id = tr.querySelector('.openitem').getAttribute("data-item-id");
    const orderid = document.querySelector('#openorder').getAttribute("data-item-id");
    console.log(orderid)
    console.log(id)
    if (this.value == '+') {
        counter.innerHTML ++;               //увеличили счетчик если нажали +
    } else if (counter.innerHTML >0) 
    {counter.innerHTML --}                  //уменьшили - если нажали - и > 0
    cnt = counter.innerHTML
    fetch(`/itemqnt/${orderid}/${id}/${cnt}/`)
    .then(response => response.json())
    .then(orderdata => {
    // Отражаем имя, описание и цену
    const price = orderdata.price;
    const description = orderdata.description;
    console.log(price)
    console.log(description)
    document.querySelector('#fprice').innerHTML = price;
    document.querySelector('#fdescription').innerHTML = description;
    })
}


function all_items() {
    // Показываем перечень items и прячем purchase_view
    document.querySelector('#purchase_view').style.display = 'none';
    document.querySelector('#all_items_view').style.display = 'block';
    const status = document.head.getAttribute('data-status');
    if (status == 'success') { 
    alert('Платеж выполнен')}
    else if (status == 'cancel') {
    alert('Платеж отменен')
    }
  }


function open_item(evnt) {
    evnt.preventDefault(); // не даем ссылке нажаться - перейти на другую страницу
    //не даем отработать кнопке заказа, если заказ пустой
    const price = parseInt(document.querySelector('#fprice').innerHTML);
    const check = this.classList.contains('openitem');
    console.log(check || price);
    if ( check || price){           
        // Показываем выбранную item и прячем all_items_view
        document.querySelector('#purchase_view').style.display = 'block';
        document.querySelector('#all_items_view').style.display = 'none';
        const id = this.getAttribute("data-item-id");
        const orderitem = this.getAttribute("data-type");
        console.log(orderitem)
        console.log(id)
        fetch(`/getitem/${orderitem}/${id}/`)
        .then(response => response.json())
        .then(itemdata => {
            // Отражаем имя, описание и цену выбранной item/order
            const itemname = itemdata.name;
            const itemdescription = itemdata.description;
            const itemprice = itemdata.price;
            document.querySelector('#name').innerHTML = itemname;
            document.querySelector('#description').innerHTML = itemdescription;
            document.querySelector('#checkout-button').innerHTML = itemprice;
            document.querySelector('#checkout-button').setAttribute('data-type', orderitem);
            document.querySelector('#checkout-button').setAttribute('data-item-id', id);
        });
    }
}


function buy_item() {
    const id = this.getAttribute("data-item-id");
    const orderitem = this.getAttribute("data-type");
    console.log(orderitem)
    console.log(id)
    fetch(`/buyitem/${orderitem}/${id}/`)
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            var stripePK = document.body.getAttribute('data-stripe-pk');
            var stripe = Stripe(stripePK);
            stripe.redirectToCheckout({
                sessionId: data.session_id
            }).then(function(result) {
                console.log(result.error.message);
            });
        });
}
