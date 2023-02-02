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



## The microservice approach微服務方法

If we were to build the same application using microservices, we would organize the code into several separate components that run in separate processes. 

如果我們使用微服務構建同一個應用程序，我們會將程式碼組織成幾個單獨的組件，這些組件在單獨的行程中運行。

We have already discussed the PDF report generator, and we can examine the rest of the application and <u>see where we could split it into different microservices,</u> as shown in the following diagram:

<img src ='../pic/microservice-model.png'>

單片應用程序的內部互動只是通過單獨的部分可見。 我們改變了一些複雜性，最終得到了以下七個獨立的組件：

1. **Booking UI**:A frontend service that generates the web user interface,an interacts with all the other microservices生成web用户界面的前端服务，与所有其他微服务交互

2. **PDF reports**:A very simple service that will create PDFs for receipts or any other document given a template and some data ,Also known as the PDF reporting service一個非常簡單的服務，它將為收據或任何其他檔案創建PDF，並提供範本和一些數據，也稱為PDF報告服務

3. **Search**:A service that can be queried to get a list of hotels when given a locatin,This service has its own database 當給定位置時，可以査詢以獲取飯店清單的服務。此服務有自己的資料庫

4. **Payments**:A service that interacts with the third-party bank serivice,and manages a biling database,It also sends emails on successful payment.一種與協力廠商銀行服務互動並管理帳單資料庫的服務，它還發送成功付款的電子郵件。

5. **Reservations**:Managers reservations and changes to bookings經理預訂和預訂更改

6. **Users**:Stores the user information,and interacts with users via emails存儲用戶資訊，並通過電子郵件與用戶互動

7. **Authentication**:An OAuth 2-based service that returns authentication tokens,which each microservice can use to authenticate when calling others 一個基於OAuth 2的服務，它返回身份驗證權杖，每個微服務可以在調用其他微服務時使用該權杖進行身份驗證

   

Those microservices, along with a few external services, like the email service, would provide a feature set similar to the monolithic application. In this design, each component communicates using the HTTP protocol, and features are made available through RESTful web services.In this design,each component communicates using the HTTP protocal,and features are made avaiable through RESTful web services.

這些微服務以及一些外部服務（如電子郵件服務）將提供類似於單片應用程序的功能集。 在這個設計中，每個組件都使用HTTP協議進行通信，並且通過RESTful web服務提供了功能。在這個設計裏，每個組件使用HTTP協議通信，並且可以通過RESTful web服務提供功能。



There's not centralized database,as each microservice deals internally with its own data structures and the data that gets in and out uses a language-agnostic format like **JSON**

沒有集中化的資料庫，因為每個微服務都在內部處理自己的資料結構，進出的數據使用JSON這樣的語言不可知格式



<u>Hers is a full definition attempt:</u>

A microservice is a lighweight application that provides a narrow list of features with a well-defined contract.It is a component with a single responsibility that can be developed and deployed independently

微服務是一個羽量級的應用程序，它提供了一個具有明確定義的契約的功能清單。它是一個具有單一職責的組件，可以獨立開發和部署



## Microservice benefits 微服務的好處

- Separation of concerns
- Smaller projects to deal with
- More scaling and deployment options

### Separation of concerns 關注點分離

First of all, each microservice can be developed independently by a separate team.

首先，每個微服務都可以由單獨的團隊獨立開發。



That also means the evolution of the app is more under control. than with monoliths 

比整體方法更有控制



This is known as loose coupling, and improves the overall project velocity as we apply, 

這被稱為松耦合，當我們在服務級別應用類似於單一責任原則的理念時，它提高了整個項目的速度。 


### Smaller projects 較小的項目

s s s s s s

The second benefit is breaking the complexity of the project. When you add a feature to an application such as PDF reporting, even if you do it cleanly, you make the code base bigger, more complicated, and sometimes slower. <u>Building that feature in a separate application avoids this problem and makes it easier to write it with whatever tools you want.</u>

在單獨的項目中構建特徵避免了這種問題，也更加容易去使用想用的工具

<u>You can refactor it often, shorten your release cycles,</u> and stay on top of things. The growth of the application remains under your control.



<u>Dealing with a smaller project also reduces risks when improving the application:</u>
 if a team wants to try out the latest programming language or framework, they can iterate quickly on a prototype that implements the same microservice API, try it out, and decide whether or not to stick with it.



<u>Reducing the size of each component also makes it easier to think about for developers</u>, especially new ones joining the team or ones who are stressed about handling an outage with the service. Instead of having to work through an entire system, a developer can focus on a smaller area and not worry about the rest of the application's features.



### Scaling and deployment 擴展和部署

Finally, having your application split into components makes it easier to scale depending on your constraints. 最後，將應用程序折開為多個組件可以更容易地根據約束進行縮放。



We can, thus, summarize the benefits of microservices as follows:

- A team can develop each microservice independently ,and use whatever technology stack makes sense.They can define a custom release cycle.All they need to define is a language-agnostic HTTP API一個團隊可以獨立開發每個微服務，並使用任何有意義的科技堆棧。他們可以定義自定義發佈週期。他們只需要定義一個語言不可知的HTTP API

- Developers split the application complexity into logical components,Each microservices focuses on doing one thing well開發人員將應用程序的複雜性劃分為邏輯組件，每個微服務都專注於做好一件事

- Since microservice are standalone applications ,there's finer control over deployments,which makes scaling easier 由於微服務是獨立的應用程序，囙此對部署有更精細的控制，這使得擴展更容易

   



## Pitfalls of microservices 微服務的陷阱

You need to be aware of these main problems you might have to deal with when coding microservices:

- Illogical splitting
- More network interactions
- Data storing and sharing
- Compatibility issues
- Testing



### Illogical splitting不合邏輯的分裂

The design needs to mature with some try-and-fail cycles. And adding and removing microservices can be more painful than refactoring a monolithic application. You can mitigate this problem by avoiding splitting your app into microservices if the split is not evident.設計需要經過一些嘗試和失敗的迴圈才能成熟。 添加和删除微服務可能比重構單一應用程序更痛苦。 如果折開不明顯，您可以通過避免將應用程序折開為微服務來緩解這個問題。







### More network interactions更多網路互動

The second problem is the number of network interactions added to build the same application.



That requires extra attention to how each backend service is called and raises a lot of questions, like the following:

- What happens when the Booking UI cannot reach the PDF reporting service because of a network split or a laggy service?當Booking UI由於網絡分裂或服務滯後而無法訪問PDF報告服務時會發生什麼？

- Does the Booking UI call the other services synchronously or asynchronously?預訂UI是同步還是非同步調用其他服務？

- How will that impact the response time?這將如何影響回應時間？

  

### Data storing and sharing数据存储和共享

Another problem is data storing and sharing. An effective microservice needs to be independent of other microservices, and ideally, <u>should not share a database.</u> What does this mean for our hotel booking app?



Again, that raises a lot of questions, such as the following:

- Do we use the same users' IDs across all database,or do we have independent IDs in each service and keep it as a hidden implementation detail?我們是在所有資料庫中使用相同的用戶ID，還是在每個服務中<u>使用獨立的ID並將其作為隱藏的實現細節？</u>
- Once a user is added to the system, do we replicate some of her information in other services' databases via strategies like data pumping, or is that overkill?一旦一個用戶被添加到系統中，我們是通過諸如數據抽取之類的策略將她的一些資訊複製到其他服務的資料庫中，還是過度使用？
- How do we deal with data removal?我們如何處理數據删除？

### Compatibility issues相容性問題

Another problem happens when a feature change impacts several microservices. If a change affects, in a backward-incompatible way, the data that travels between services, you're in for some trouble.



### Testing測試

 You can't fully test things out with just one piece of the puzzle, although having a clean and well-defined interface does help.你不可能只用一塊拼圖就完全測試出來，儘管擁有一個乾淨且定義良好的介面確實有幫助。





The pitfalls of using microservices can be summarized as follows:

- Premature splitting of an application into microservices can lead to architectural problems.過早地將應用程序折開為微服務可能會導致架構問題。
- Network interactions between microservices add potential points of failure and additional overhead.微服務之間的網絡互動新增了潜在的故障點和額外的開銷。
- Testing and deploying microservices can be complex.測試和部署微服務可能很複雜。
- And the biggest challenge—data sharing between microservices is hard.微服務之間最大的挑戰是資料共用。





## Implementing microservices with Python 用Python實現微服務

> 好處

Python is an amazingly versatile language. As you probably already know, Python is used to build many different kinds of applications – from simple system scripts that perform tasks on a server to large object-oriented applications that run services for millions of users. 

> 缺點

However, some developers criticize Python for being slow and unfit for building efficient web services



### How web services workweb服務如何工作

> If we imagine a simple program that answers queries on the web, the description
>  is straightforward. A new connection is made, and the protocol is negotiated. A request is made, and some processing is done: perhaps a database is queried. Then a response is structured and sent, and the connection is closed. This is often how we want to think about our application's logic, because it keeps things simple for the developer as well as anyone else responsible for the program once it's running.
>
> The web is a big, complicated place, though. Various parts of the internet will try to do malicious things to a vulnerable web service they find. Others just behave badly because they have not been set up well. Even when things are working well, there are different HTTP protocol versions, encryption, load balancing, access control, and a whole set of other things to think about.
>
> Rather than reinvent all of this technology, there are **interfaces** and **frameworks** that let us use the tools that other people have built, and spend more of our time working on our own applications. They let us use web servers such as **Apache** and **nginx** and let them handle the difficult parts of being on the web, such as certificate management, load balancing, and handling multiple website identities. Our application then has a smaller, more manageable configuration to control
>
> its behavior.





### The WSGI standard WSGI標準

Inspired by the older **Common Gateway Interface** (**CGI**), <u>the Python web community has created a standard called the **Web Server Gateway Interface** (**WSGI**)</u>. It simplifies how you can write a Python application in order to serve HTTP requests. When your code uses this standard, your project can be executed by standard web servers like Apache or nginx, using WSGI extensions like uwsgi or mod_wsgi.



Your application just has to deal with incoming requests and send back JSON responses, and Python includes all that goodness in its standard library.

您的應用程序只需要處理傳入的請求並發回JSON響應，Python在其標準庫中包含了所有這些優點。



You can create a fully functional microservice that returns the server's local time with a vanilla Python module of fewer than 10 lines:您可以使用少於10行的普通Python模塊創建一個功能齊全的微服務，返回服務器的本地時間：

```python
import time 
import json 
def application(environ,start_response):
  headers =[('Content-type','applications/json')]
  start_response('200 ok',headers)
  return [bytes(json.dumps({"time":timetime()}),'utf8')]

```

<u>The biggest problem with WSGI, though, is its synchronous nature.</u> More recently, the **Asynchronous Server Gateway Interface** (**ASGI**) has emerged as a successor to WSGI, allowing frameworks to operate asynchronously with the same seamless behavior as before. What are synchronous and asynchronous applications? We will cover that now.<u>然而，WSGI最大的問題是其同步性</u>。 最近，非同步服務器閘道介面（ASGI）已成為WSGI的繼承者，允許框架以與以前相同的無縫行為非同步操作。 什麼是同步和非同步應用程序？ 我們現在就來報導。



### Workers,threads and synchronicity 工作、線程和同步性

Thinking back to our simple application that handles requests, our model of the program is synchronous. This means that it accepts a piece of work, does that work, and returns the result, <u>but while it's doing all of that, the program can't do anything else. Any other requests that come in when it's already working on something will have to wait.</u>

回想一下我們處理請求的簡單應用程序，我們的程式模型是同步的。 這意味著它接受一段工作，執行該工作，並返回結果，但當<u>它執行所有這些工作時，程式不能執行任何其他操作。 當它已經在處理某件事情時，任何其他請求都必須等待</u>。

解決方法有以下幾點，工作池是早期的方法，最近使用的都是非同步python



#### A worker pool approach工作池方法

Accepting a new request is often very fast, and the bulk of the time is taken up by doing the work that has been requested. Reading a request that tells you "Give me a list of all our customers in Paris" takes much less time than putting the list together and sending it back.

接受新的請求通常很快，大部分時間都被完成請求的工作所佔用。 閱讀一份告訴你“給我一份我們在巴黎的所有客戶的名單”的請求，所花的時間要比把名單放在一起並寄回要少得多。

**<u>When an application has lots of requests arriving, an effective strategy is to ensure that all the heavy lifting is done using other processes or threads.</u>** 當應用程序有大量請求到達時，一個有效的策略是確保所有繁重的工作都使用其他行程或線程完成。



這個一個老技術但是有效率。不過他的缺點是

As far as each worker is concerned, it receives work, and can't do anything else until it has finished. <u>This means that if you have eight worker processes, you can only handle eight simultaneous requests.</u> Your application could create more workers if it is running low, but there is always a bottleneck.

就每個工人而言，他們都接受工作，在完成之前不能做任何其他事情。 這意味著，<u>如果您有八個工作行程，則只能同時處理八個請求。</u> 如果應用程序運行速度低，它可能會創建更多的工作人員，但始終存在瓶頸。



There is also a practical limit to the number of processes and threads that an application can create, and swapping between them takes a lot of time that a responsive application can't always afford.

應用程序可以創建的行程和線程的數量也有實際的限制，並且它們之間的交換需要大量的時間，而響應應用程序總是無法承受。



#### Being asymchronous 不同步的

You don't really want to be sitting there doing nothing while waiting for an answer, but that's what a process usually does if it's synchronous. An asynchronous program is aware that some tasks it has been told to perform might take a long time, and so it can get on with some other work while it is waiting, without necessarily having to use other processes or threads.

你真的不想坐在那裡等待答案，但如果行程是同步的，那麼它通常會這樣做。 非同步程式知道被告知執行的某些任務可能需要很長時間，囙此它可以在等待時繼續執行其他工作，而不必使用其他行程或線程。


#### Twisted,Tornado,Greenlets and Gevent 

For a long time,non-WSGI framworks like Twisted and Tornado were the popular answers for concurrency when using Python.allowing developers to specify **callbacks** for many simultaneous requests.

很長一段時間以來，Twisted和Tornado等非WSGI框架是使用Python時併發性的流行答案。允許開發人員為許多同時請求指定**callback**。



A callback is a technique where the calling part of the program doesn't wait but instead tells the function what it should do with the result it generates. Often this is another function that it should call.

callback是一種科技，程式的調用部分不等待，而是告訴函數它應該對生成的結果做什麼。 通常這是它應該調用的另一個函數。





#### Asynchronous Python非同步Python

Python 3 has introduced a full set of features and helpers in the asyncio package to build asynchronous applications; 

**aiohttp** is one of the most mature asyncio packages,and building the earlier 'time' microservice with it would simply need these lines

Aiohttp是最成熟的非同步包之一，用它構建早期的“time”微服務只需要以下幾行

```python
from aiohttp import web 
import time 
async def handle(request):
  return web.json_response({'time':time.time()})

if __name__ =="__main__":
  app = web.application()
  app.router.add_get("/",handle)
  web.run_app(app)
```

在這個小示例中，我們非常接近如何實現同步應用程序。 我們使用非同步程式碼的唯一提示是async關鍵字，它將控制碼函數標記為協程。



這一概念將在非同步Python應用程序的每一個級別上使用。 下麵是另一個使用aiogg的示例，aiogg是項目檔案中用於非同步的PostgreSQL庫：



```python
import asyncio
import aiopg 

dsn = "dbname=postgres user=postgres password=mysecretpassword
host=127.0.0.1"
async def go():
  pool = await aiopg.create_pool(dsn)
  async with pool.acquire() as conn:
    async with conn.cursor() as cur:
      await cur.excute("select 1 ")
      ret = []
      async for row in cur:
        ret.append(row)
      assert ret ==[(1,)]
  await pool.clear()
  
loop = asyncio.get_event_loop()
loop.run_until_complete(go())
```

With a few async and await prefixes, the function that performs an SQL query and sends back the result looks a lot like a synchronous function. We will explain more about this code in later chapters.

通過幾個非同步和等待首碼，執行SQL査詢並返回結果的函數看起來很像同步函數。 我們將在後面的章節中詳細解釋此程式碼。

### Language performace 語言表現

每個人都知道Python比Java或Go慢，但執行速度並不總是最重要的。 微服務通常是一個薄薄的程式碼層，它大部分時間都在等待其他服務的網絡響應。 它的覈心速度通常不如SQL査詢從Postgres服務器返回的速度重要，因為後者將代表構建響應所花費的大部分時間。

但想要一個盡可能快的應用程序是合理的。
Python社區中關於加速語言的一個有爭議的話題是**全域解譯器鎖（GIL）**如何影響效能，因為多執行緒應用程序不能使用多個行程。
GIL有充分的理由存在。 它**<u>保護CPython解譯器的非執行緒安全部分，並存在於Ruby等其他語言中。 到目前為止，所有删除它的嘗試都未能產生更快的CPython實現。</u>**



# Chapter2: Discovering Quart 探索Quart

>  **Quart** was started in 2017 as an evolution of the popular **Flask** framework. Quart shares many of the same design decisions as Flask, and so a lot of the advice for one will work with the other. This book will focus on Quart to allow us to support asynchronous operations and to explore features such as WebSockets and HTTP/2 support.

Quart是Flask的變種

A typical example of this philosophy is when you need to interact with a SQL database. A framework such as Django is batteries-included and provides everything you need to build your web app, including an **Object-Relational Mapper** (**ORM**) to bind objects with database query results.



### How Quart handles requestsQuart如何處理請求 



### Quart's built-in featuresQuart的內寘功能



### A microservice skeleton微服務框架

