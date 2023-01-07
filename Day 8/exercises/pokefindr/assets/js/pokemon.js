async function getPokemon(){

    id = "" // TODO: get ID from query parameters

    pokemonData = {
        name:"",
        image:"",
        id:id,
        description:""
    }
    
    // Documentation https://pokeapi.co/docs/v2#pokemon-species
    await fetch(`https://pokeapi.co/api/v2/pokemon-species/${id}/`)
      .then((response) => response.json())
          .then((data) => {
            // TODO: Get description from data
            pokemonData.description = ""
            
          }
        )
    
    // Documentation: https://pokeapi.co/docs/v2#pokemon
    await fetch(`https://pokeapi.co/api/v2/pokemon/${id}/`)
      .then((response) => response.json())
          .then((data) => {
            // TODO: Get image and name from data
            pokemonData.image = ""
            pokemonData.name = ""
          }
        )
    return pokemonData
}

async function loadData(){
    pokeData = await getPokemon()
    console.log("input data", pokeData)
    console.log("name", pokeData.name)
    console.log("id", pokeData.name)
    console.log("image", pokeData.name)
    console.log("description", pokeData.name)
    
    document.getElementById("pokemon-name").innerHTML = pokeData.name
    document.getElementById("pokemon-image").src = pokeData.image
    document.getElementById("pokemon-description").innerHTML = pokeData.description
    document.getElementById("pokemon-id").innerHTML= `#${pokeData.id}`
    document.getElementById("bulbapedia-link").href= `https://bulbapedia.bulbagarden.net/wiki/${pokeData.name}`
}