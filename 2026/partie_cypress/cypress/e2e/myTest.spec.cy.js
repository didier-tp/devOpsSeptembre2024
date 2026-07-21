//NB: il faut préalablement lancer le serveur (via docker ou pas)
describe('My cypress Tests', () => {
it('good mensualite', () => {
//partir de index.html
cy.visit("http://127.0.0.1:5000/static/index.html")
//cliquer sur le lien comportant 'basic'
cy.contains('empruntAjax').click()
cy.wait(50)

// Get an input, type data into it
//and verify that the value has been updated
cy.get('input[id="inputMontant"]')
.clear()
.type('10000')
.should('have.value', '10000')

cy.get('input[id="inputDuree"]')
.clear()
.type('60')
.should('have.value', '60')

cy.get('input[id="inputTaux"]')
.clear()
.type('2')
.should('have.value', '2')

//declencher click sur bouton btnMensualite
cy.get('button[id="btnMensualite"]')
.click()
//vérifier que la zone d'id spanRes comporte le texte '175.....'
cy.get('#spanRes')
.should('have.text', '175.27760053243998')
})
})