

document.addEventListener('DOMContentLoaded', function () {
    // Get the category field and pdfID element
    const categoryField = document.getElementById('article-cat');
    const pdfField = document.getElementById('article-id');
    const labelId = document.getElementById('label-id');
    const conTentField = document.getElementById('artcile_content');
    const labelContent = document.getElementById('label-content');
    const magazinField = document.getElementById('magazin-id')
    const labelMagazin = document.getElementById('label-magazin')
    const puplished_dayField = document.getElementById('puplished_day-id')
    const labelPuplished_day = document.getElementById('label-puplished_day')

    if (categoryField && pdfField) {
        // Function to update the pdfID display based on category value
        const updatePdfFieldDisplay = () => {
            const selectedValue = categoryField.value;
            if (selectedValue === '2') {
                pdfField.classList.add('d-none'); // Hide element
                labelId.classList.add('d-none'); // Hide element
                pdfField.classList.remove('d-flex'); // Remove display:flex
                labelId.classList.remove('d-flex'); // Remove display:flex

                conTentField.classList.add('d-flex');
                labelContent.classList.add('d-flex');
                conTentField.classList.remove('d-none');
                labelContent.classList.remove('d-none');

                magazinField.classList.add('d-none');
                labelMagazin.classList.add('d-none');
                magazinField.classList.remove('d-flex');
                labelMagazin.classList.remove('d-flex');

                puplished_dayField.classList.add('d-none');
                labelPuplished_day.classList.add('d-none');
                puplished_dayField.classList.remove('d-flex');
                labelPuplished_day.classList.remove('d-flex');


            } else if (selectedValue === '1') {
                pdfField.classList.add('d-flex'); // Show element
                labelId.classList.add('d-flex'); // Show element
                pdfField.classList.remove('d-none'); // Remove display:none
                labelId.classList.remove('d-none'); // Remove display:none

                conTentField.classList.add('d-none');
                labelContent.classList.add('d-none');
                conTentField.classList.remove('d-flex');
                labelContent.classList.remove('d-flex');

                magazinField.classList.add('d-flex');
                labelMagazin.classList.add('d-flex');
                magazinField.classList.remove('d-none');
                labelMagazin.classList.remove('d-none');

                puplished_dayField.classList.add('d-flex');
                labelPuplished_day.classList.add('d-flex');
                puplished_dayField.classList.remove('d-none');
                labelPuplished_day.classList.remove('d-none');
            }
        };

        // Trigger update on page load (optional)
        updatePdfFieldDisplay();

        // Add event listener for changes in the category field
        categoryField.addEventListener('change', updatePdfFieldDisplay);
    }
});

