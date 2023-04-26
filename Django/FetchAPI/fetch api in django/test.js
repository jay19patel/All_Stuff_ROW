console.log("runing..")

async function postData(url, data) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });
    return response.json();
  }
  
function adddata(){
  postData('api', {name: 'John', age: 30})
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error(error);
    });
}
  
  
  
