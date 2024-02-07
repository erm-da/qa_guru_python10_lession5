from selene import browser, have, be, by
import os

def test_demoqa():
    browser.open("/")
    browser.element('#firstName').should(be.blank).type('Denis')
    browser.element('#lastName').should(be.blank).type('Ermakov')
    browser.element('#userEmail').should(be.blank).type('dermakov@test.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('7911001020')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('option[value="11"]').click()
    browser.element('.react-datepicker__year-select').element('option[value="1992"]').click()
    browser.element('.react-datepicker__day--005').click()
    browser.element('#subjectsInput').type("Computer").press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('stock_img.jpg'))
    browser.element('#currentAddress').type("Saint-Petersburg")
    browser.element('#state').click().element(by.text("NCR")).click()
    browser.element('#city').click().element(by.text("Delhi")).click()
    browser.element('#submit').click()

    #Assert
    browser.element('.table-responsive').should(have.texts(
        "Denis Ermakov",
        "dermakov @ example.com",
        "Male",
        "7911001020",
        "05 December,2024",
        "Computer Science",
        "Sports, Reading, Music",
        "stock_img.jpg",
        "Saint-Petersburg",
        "NCR Delhi"

    ))



