> example code:
>
> https://github.com/PacktPublishing/Python-Microservices-Development-2nd-Edition

# Chapter 1: Understanding Microservices

Microservices have revolutionized software products by improving the readability and scalability of services ,and have allowed organizations to speed up their release cycles  and be more responsive to the needs of their customers. 

微服務通過提高服務的可讀性和可擴展性，徹底改變了軟體產品，並使組織能够加快其發佈週期，對客戶的需求做出更大的響應。



隨著成千上萬的客戶同時使用您的服務，將一項試驗性功能推向生產並在需要時再次删除它被認為是一種良好的做法，而不是等待數月才能同時發佈它和許多其他功能。





## The origins of service-oriented architecture面向服務架構的起源

There is no official standard for microservices ,so it is helpful to look at a bit of the history in this area of software design.

When discussing microservices,Service-Oriented Architecture(SOA) is often used as a starting point.

當談論到微服務，面向服務架構總會是起源點。



SOA is a way of thinking about software architecture that encourages reusable software components that provide well-defined interfaces. This allows those components to be reused and applied to new situations。

SOA是一種思考軟件架構的管道，它鼓勵提供定義良好的介面的可重用軟件組件。 這允許重用這些組件並將其應用於新情况

SOA services could communicate via **Inter-Process Communication** (**IPC**) using sockets on the same machine, through shared memory, through indirect message queues, or even with **Remote Procedure Calls** (**RPC**). The options are extensive, and SOA is a useful set of principles for a wide variety of situations.

SOA服務可以通過行程間通信（IPC），使用同一台機器上的通訊端，通過共用記憶體，通過間接消息隊列，甚至通過遠程過程調用（RPC）進行通信。 選項非常廣泛，SOA是一套適用於各種情况的有用原則。

> if we want ot give a complete definition of microservices ,the best way to understand it is in the context of different software architectures,



## The monolithic approach整體方法

With a monolith, everything about the service is in one place – the API, database, and all associated tools are managed as part of one code base.



<u>用一個網頁預定酒店的例子來理解整體方法</u>

When a user performs a search on the hotel website,the application goes through the following steps:當用戶在飯店網站上執行搜索時，應用程序將執行以下步驟：

1. It runs a couple of SQL queries against its hotel database 
2. An HTTP request is made to a partners's service to add more hotels to the list 
3. Results are sent to the JavaScript embedded in the web page,to render the information for the viewer

From there once,the user has found the perfect hotel and selected the booking option,the application performs these steps:一旦用戶找到了理想的飯店並選擇了預訂選項，應用程序將執行以下步驟：

1. The customer gets created in the database,if needed,and has to authenticate
2. Payment is carried out by interacting with the bank's web service
3. The app saves the payment details in the database for legal reasons
4. A receipt is generated using a PDF generator 
5. A recap email is sent to the user using the email service
6. A reservation email is forwarded to the third-party hotel using the email service
7. A database entry is added to keep track of the reservation

該應用程序與包含飯店資訊、預訂詳情、帳單、用戶資訊等的資料庫互動。它還與外部服務互動，用於發送電子郵件、付款以及從合作夥伴處獲取更多飯店。

在Web早期，一項服務經常使用**<u>LAMP(Linux-Apache-MySQL-Perl/PHP/Python)</u>**架構

<img src ='../pic/LAMP.png'>

這種架構還有很多優點的，比如說結構簡單啦，對項目進行測試很簡單，還能重新調整模型架構，還能調整模型，設置什麼格式的輸入



如果你的應用stay small，這種模型表現較好，對一個團隊來說<u>.But projects usually grow,and they get bigger than what was first intended,And having the whole application in a single code base brings some nasty issues along the way</u>。但項目通常會增長，而且比最初的預期要大，而且將整個應用程序放在一個代碼庫中會帶來一些棘手的問題

> For instance, if you need to make a sweeping change that is large in scope, such as changing your banking service or your database layer, the risks impact the whole application. These changes can have a huge impact on the project and need to be tested well before being deployed, and such testing often can't be exhaustive. Changes like this will happen in a project's life.
>
> 例如，如果您需要進行範圍較大的全面更改，例如更改您的銀行服務或資料庫層，則風險會影響整個應用程序。 這些更改可能會對項目產生巨大影響，需要在部署之前進行良好的測試，並且此類測試通常無法窮盡。 這樣的變化將在項目的生命週期中發生。



總結來說，整體架構的優點有

- Starting a project as a monolith is easy,and probably the best approach作為一個整體開始一個項目很容易，而且可能是最好的方法
- A centeralized database simplifies the design and organization of the data中心化數據庫簡化了數據的設計和組織
- Deploying one application is simple部署一個應用程序很簡單

對應的缺點有

- Any change in the code can impact unrelated features.When something breaks,the whole application may break程式碼中的任何更改都會影響不相關的功能。當某些東西發生故障時，整個應用程序可能會崩潰

- Solutions to scale your appliction are limited:you can deploy serval instances,but if one particular feature inside the app takes all the resources,it impacts everything 擴展應用程序的解決方案是有限的：您可以部署幾個實例，但如果應用程序中的某個特定功能佔用了所有資源，則會影響所有內容

- As the code base grows,it's hard to keep it clean and under control隨著代碼庫的增長，很難保持其乾淨和受控

  

面對以上問題，提出的方法有：

最顯著的方法是將項目分為單獨的模塊，即使所有代碼都在一個管道工作。Developers do this by building their apps with external libraries and frameworks. Those tools can be in-house or from the **Open-Source Software** (**OSS**) community.開發人員通過使用外部庫和框架構建應用程序來實現這一點。 這些工具可以是內部的，也可以來自開源軟件（OSS）社區。



## The microservice approach

If we were to build the same application using microservices, we would organize the code into several separate components that run in separate processes. 

如果我們使用微服務構建同一個應用程序，我們會將程式碼組織成幾個單獨的組件，這些組件在單獨的行程中運行。

We have already discussed the PDF report generator, and we can examine the rest of the application and <u>see where we could split it into different microservices,</u> as shown in the following diagram:

<img src ='../pic/microservice-model.png'>

單片應用程序的內部互動只是通過單獨的部分可見。 我們改變了一些複雜性，最終得到了以下七個獨立的組件：

1. Booking UI:

2. PDF reports:

3. Search:

4. Payments:

5. Reservations:

6. Users:

7. Authentication:

   

## Microservice benefits 



## Pitfalls of microservices 



## Implementing microservices with Python 

