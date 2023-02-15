function addToCart(name, price, sale, description, image){
    // Adds an item to the "cart"
    inDatabase = window.localStorage.getItem(name)
    if (!inDatabase){
        window.localStorage.setItem(name, JSON.stringify({"price":price, "sale":sale, "description":description, "image":image, "quantity":1}))
    } else{
        inDatabase = JSON.parse(inDatabase)
        inDatabase["quantity"] += 1
        window.localStorage.setItem(name, JSON.stringify(inDatabase))
    }
}

function getCart(){
    // Searches the localStorage database for items from the cart
    cart = []
    for (key in localStorage){
        if (!(["length","clear","getItem","key","removeItem","setItem"].includes(key))){
            values = JSON.parse(window.localStorage.getItem(key))
            values.name = key
            cart.push(values)
        }
    }
    return cart
}

function removeFromCart(name){
    // Adds an item to the "cart"
    inDatabase = window.localStorage.getItem(name)
    if (!inDatabase){
        return // Nothing to remove
    }else{
        inDatabase = JSON.parse(inDatabase)
        if (inDatabase["quantity"] > 1){
            inDatabase["quantity"] -= 1
            window.localStorage.setItem(name, JSON.stringify(inDatabase))
        } else{ // No more of the item in the DB
            window.localStorage.removeItem(name)
        }
    }
}
