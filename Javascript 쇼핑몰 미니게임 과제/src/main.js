
//Fetch the items from the JSON file
function loadItems() {
    return fetch('data/data.json') 
    .then(response => response.json())
    .then(json => json.items);
    
} //fetch 사용법 더 공부하기


//main
loadItems()
.then(items => {
    console.log(items);
    displayItems(items);
    setEventListeners(items)
})
.catch(console.log);