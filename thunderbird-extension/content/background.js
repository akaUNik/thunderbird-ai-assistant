browser.messageDisplayAction.onClicked.addListener((tab) => {
    browser.messageDisplay.getDisplayedMessage(tab.id).then((message) => {
        browser.windows.create({
            url: "content/popup.html",
            type: "popup",
            width: 500,
            height: 600
        });
    });
});