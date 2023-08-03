document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.querySelector(".menu-toggle");
  const navWrapper = document.querySelector(".nav-wrapper");
  const header = document.querySelector("header");
  const base = document.querySelector(".base");
  const footer = document.querySelector(".page-footer");
  const teamHeading = document.querySelector(".team-heading");
  const teamParagraph = document.querySelector(".team-paragraph");
  const meetTheTeamContainer = document.querySelector(".meet-the-team-container");

  menuToggle.addEventListener("click", function () {
    navWrapper.classList.toggle("open");

    // Adjust the main content and .meet-the-team-container to shrink when the navbar is open
    const isOpen = navWrapper.classList.contains("open");
    if (isOpen) {
      header.style.transform = "scale(0.8)";
      base.style.transform = "scale(0.8)";
      footer.style.transform = "scale(0.8)";
      teamHeading.style.transform = "scale(0.8)";
      teamParagraph.style.transform = "scale(0.8)";
      meetTheTeamContainer.style.transform = "scale(0.8) translateY(10%)";
    } else {
      header.style.transform = "scale(1)";
      base.style.transform = "scale(1)";
      footer.style.transform = "scale(1)";
      teamHeading.style.transform = "scale(1)";
      teamParagraph.style.transform = "scale(1)";
      meetTheTeamContainer.style.transform = "scale(1) translateY(0%)";
    }
  });
});
