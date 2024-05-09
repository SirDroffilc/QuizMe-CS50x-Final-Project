// modify_quiz.html <<

const changeTitleButton = document.getElementById('changeTitleButton');
const changeQuizTitleForm = document.getElementById('changeQuizTitleForm');
const updateInstrucButton = document.getElementById('updateInstrucButton');
const updateQuizInstrucForm = document.getElementById('updateQuizInstrucForm');
const addQuestionButton = document.getElementById('addQuestionButton');
const addQuestionForm = document.getElementById('addQuestionForm');
const deleteQuizButton = document.getElementById('deleteQuizButton');
const deleteQuizForm = document.getElementById('deleteQuizForm');

function hideAllForms() {
    changeQuizTitleForm.style.display = 'none';
    updateQuizInstrucForm.style.display = 'none';
    addQuestionForm.style.display = 'none';
    deleteQuizForm.style.display = 'none';
}

changeTitleButton.addEventListener('click', function() {
    hideAllForms();
    changeQuizTitleForm.style.display = 'block';
})

updateInstrucButton.addEventListener('click', function() {
    hideAllForms();
    updateQuizInstrucForm.style.display = 'block';
})

addQuestionButton.addEventListener('click', function() {
    hideAllForms();
    addQuestionForm.style.display = 'block';
})

deleteQuizButton.addEventListener('click', function() {
    hideAllForms();
    deleteQuizForm.style.display = 'block';
})

// >>