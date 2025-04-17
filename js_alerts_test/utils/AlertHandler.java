package utils;

import org.openqa.selenium.Alert;
import org.openqa.selenium.WebDriver;

public class AlertHandler {

    WebDriver driver;

    public AlertHandler(WebDriver driver) {
        this.driver = driver;
    }

    public String handleAlert(String action, String inputText) {
        Alert alert = driver.switchTo().alert();
        String alertText = alert.getText();

        switch (action.toLowerCase()) {
            case "accept":
                alert.accept();
                break;
            case "dismiss":
                alert.dismiss();
                break;
            case "sendkeys":
                alert.sendKeys(inputText);
                alert.accept();
                break;
            default:
                System.out.println("Invalid alert action");
        }
        return alertText;
    }
}
