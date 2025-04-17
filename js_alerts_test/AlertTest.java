import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import utils.AlertHandler;

public class AlertTest {
    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        driver.get("https://the-internet.herokuapp.com/javascript_alerts");

        AlertHandler alertHandler = new AlertHandler(driver);

        driver.findElement(By.xpath("//button[text()='Click for JS Alert']")).click();
        String alert1Text = alertHandler.handleAlert("accept", null);
        System.out.println("Alert1 Text: " + alert1Text);
   
        driver.findElement(By.xpath("//button[text()='Click for JS Confirm']")).click();
        String alert2Text = alertHandler.handleAlert("dismiss", null);
        System.out.println("Alert2 Text: " + alert2Text);
   
        driver.findElement(By.xpath("//button[text()='Click for JS Prompt']")).click();
        String alert3Text = alertHandler.handleAlert("sendkeys", "Hello");
        System.out.println("Alert3 Text: " + alert3Text);
		
    }
}
