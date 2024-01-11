const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const iconClose = document.querySelector('.icon-close');
const loginbtn = document.querySelector('.navigation .btnlogin');
const labLink = document.querySelector('.lab-link');
const theoryLink = document.querySelector('.theory-link');
const dLink = document.querySelector('.dlab-link');
const dnoLink = document.querySelector('.dlabno-link');


loginbtn.addEventListener('click', ()=>{
    wrapper.classList.add('active-popup');
})

iconClose.addEventListener('click', ()=>{
    wrapper.classList.remove('active-popup');
})

registerLink.addEventListener('click', ()=>{
    wrapper.classList.add('active');
})

loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active');
})

labLink.addEventListener('click', ()=>{
    wrapper.classList.add('active-1');
})

theoryLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active-1');
})

dLink.addEventListener('click', ()=>{
    wrapper.classList.add('active-2');
})

dnoLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active-2');
})
