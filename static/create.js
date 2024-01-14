// let sidebar = document.querySelector(".sidebar");
// let closeBtn = document.querySelector("#btn");
// let searchBtn = document.querySelector(".bx-search");
// let logo = document.querySelector(".log")
// function menuBtnChange() {
//     if (sidebar.classList.contains("open")) {
//       closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
//     } else {
//       closeBtn.classList.replace(" ");
//       document.querySelector('.sidebar placeholder').value = '';
//     }
//   }
  
// // Open the navbar on page load
// sidebar.classList.add("open");

// closeBtn.addEventListener("click", ()=>{
//   sidebar.classList.toggle("open");
//   menuBtnChange();//calling the function(optional)
// });

// searchBtn.addEventListener("click", ()=>{ // Sidebar open when you click on the search iocn
//   sidebar.classList.toggle("open");
//   menuBtnChange(); //calling the function(optional)
// });

// // following are the code to change sidebar button(optional)
// // function menuBtnChange() {
// //  if(sidebar.classList.contains("open")){
// //    closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");//replacing the iocns class
// //  }else {
// //    closeBtn.classList.replace("bx-menu-alt-right","bx-menu");//replacing the iocns class
// //  }
// // }
// closeBtn.addEventListener("click", ()=>{
// logo.classList.toggle("active");

//   });



const container = document.querySelector(".container");
const privacy = container.querySelector(".post .privacy");
const arrowBack = container.querySelector(".audience .arrow-back");
const homesec = document.querySelector(".home-section");


window.addEventListener('resize', function(event) {
  var width = window.innerWidth;
  var sidebar = document.querySelector('.sidebar');
  var right = document.querySelector('.rightside');
  
  if (width < 768) { // or any desired width for mobile devices
    sidebar.classList.remove('open');
    right.style.display = "none"
  } else {
    sidebar.classList.add('open');
    right.style.display = "block"
  }
});






privacy.addEventListener("click", () => {
  container.classList.add("active");
});

arrowBack.addEventListener("click", () => {
  container.classList.remove("active");
});

function show_list1() {
  homesec.classList.toggle("hide");
  var postContainer = document.querySelector(".container");
  postContainer.classList.toggle("hide");
}




      // function show_list2() {
      //   var icon = document.querySelector(".like i");
      //   if (icon.classList.contains("fa-regular")) {
      //     icon.classList.remove("fa-regular");
      //     icon.classList.remove("fa-heart");
      //     icon.classList.add("fa-solid");
      //     icon.classList.add("fa-heart");
      //   } else {
      //     icon.classList.remove("fa-solid");
      //     icon.classList.remove("fa-heart");
      //     icon.classList.add("fa-regular");
      //     icon.classList.add("fa-heart");
      //   }
      // }




      // Get all the like buttons
const likeButtons = document.querySelectorAll('.like');

// Add event listeners to all the like buttons
likeButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Get the heart icon inside the button
    const heartIcon = button.querySelector('i');

    // Toggle the class of the heart icon
    heartIcon.classList.toggle('fa-regular');
    heartIcon.classList.toggle('fa-solid');
  });
});



    // Get all the like buttons
    const saveButtons = document.querySelectorAll('.save');

    // Add event listeners to all the like buttons
    saveButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Get the heart icon inside the button
        const saveIcon = button.querySelector('i');
    
        // Toggle the class of the heart icon
        saveIcon.classList.toggle('fa-regular');
        saveIcon.classList.toggle('fa-solid');
      });
    });