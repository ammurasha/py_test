const block= document.getElementById('block')
console.dir(block.textContent)

setTimeout(()=>{
  addStyles1To(block)
},2500)

block.onclick = () => {
  addStyles2To(block)
}

block.addEventListener('dblclick', () => {
  addStyles1To(block)
})

function addStyles1To(temp) {
  temp.textContent = 'edited with JS'
  temp.style.color='#006699'
  temp.style.backgroundColor='black'
}

function addStyles2To(temp) {
  temp.textContent = 'after click'
if (temp.style.backgroundColor==='red') {
  temp.style.color='#006699'
  temp.style.backgroundColor='yellow'
} else {
  temp.style.color='#FFFF00'
  temp.style.backgroundColor='red'
}
}

var re = /.+\s(\w+)\s(\w+).+/;
var str = "First Second Third Forth John Smith";
var newstr = str.replace(re, "$2, $1");
console.log(newstr);
