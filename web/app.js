function play(station){

const player=document.getElementById("player")

player.src=`http://localhost:8000/${station}`
player.play()

}

async function loadQueue(){

const res=await fetch("/api/requests")
const data=await res.json()

const list=document.getElementById("queue")
list.innerHTML=""

data.forEach(song=>{
let li=document.createElement("li")
li.innerText=song
list.appendChild(li)
})

}

setInterval(loadQueue,3000)