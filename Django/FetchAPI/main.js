console.log("Runing...")
// youtube channel : https://www.youtube.com/watch?v=a8tsXX6nvw4
//  apis
// https://jsonplaceholder.typicode.com/todos/1


// best syntext for fetch api 
// function adddata(){
//     console.log("btn clicked")

//     const promise = fetch('/api.txt')
//     .then((res) => {
//         if(!res.ok){
//             throw Error(res.statusText)
//         }
//          create response 
//         console.log(res) 
//         return res.text()})

//     .then((data) => {
//         console.log(data)
//     }).catch((error)=> {console.log(error)})
//     console.log(promise)
// }


// async and await function 
// async function adddata(){
//     try{
//         console.log("btn clicked")
//         const res = await fetch('https://jsonplaceholder.typicode.com/todos/1')
//         // response print 
//         console.log(res)
//         if(!res.ok){
//             throw Error(res.statusText)
//         }
//         // fetch data only from apis 
//         const data = await res.json()
//         document.getElementById('mydata').innerHTML = data.title
//         console.log(data)
//     }catch(error){
//         console.log(error)
//     }
// }


// async and await for each  and show in html function
// async function adddata(){
//     try{
//         console.log("btn clicked")
//         const res = await fetch('https://jsonplaceholder.typicode.com/todos/')
//         // response print 
//         console.log(res)
//         if(!res.ok){
//             throw Error(res.statusText)
//         }
//         // fetch data only from apis 
//         const data = await res.json()
//         console.log(data)
//         let output = document.getElementById('mydata');
//         data.forEach(element => {
//             // console.log("id",element.id)
//             // console.log("id",element.title)
//             output.innerHTML +=`
//             <div>Id: ${element.id}</div>
//             <div>Title : ${element.title}</div>
//             <hr>
//             `            
//         });
//     }catch(error){
//         console.log(error)
//     }
// }


// promise POST

// function adddata(){
//         console.log("btn clicked")
//         const myInit ={
//             // post means frontend thi backend ma jay using API
//             method:'POST',
//             headers:{
//                 'Content-Type':'application/json'
//             },
//             body:'{"name","jay","job":"it"}'
//         }
//         fetch('/test.html',myInit)
//         .then((res)=>{
//             if(!res.ok){
//                 throw Error(res.statusText)
//             }
//             return res.json()
//         }).then((data)=>{ 
//             console.log(data)
//         }).catch((error) => console.log(error))
    
//     }


// async with postmethod
//  BEST METHOD 
// async function postData(url, data) {
//     const response = await fetch(url, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(data)
//     });
//     return response.json();
//   }
  

// //   run function and call the async function with data 
// function adddata(){
//   postData('api', {name: 'John', age: 30})
//     .then(data => {
//       console.log(data);
//     })
//     .catch(error => {
//       console.error(error);
//     });
// }
  
  
  
