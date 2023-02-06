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

The framework entry point is the Quart class in the quart.app module. Running a Quart application means running one single instance of this class, which will take care of handling incoming **Asynchronous Server Gateway Interface** (**ASGI**) and **Web Server Gateway Interface** (**WSGI**) requests, dispatch them to the right code, and then return a response. 

框架入口點是Quart.app模塊中的Quart類。 運行Quart應用程序意味著運行這個類的一個實例，它將負責處理傳入的非同步服務器閘道介面（ASGI）和Web服務器閘道介面（WSGI）請求，將它們分派到正確的程式碼，然後返回響應。

下面是一個基本的例子

```python

from quart import Quart,request,jsonify 

app = Quart(__name__)

@app.route("/api",provide_automatic_options = False)
async def my_microservice():
    print(dir(request))
    response = jsonify({"hello":'world'})
    print(response)
    print(await response.get_data())
    return response

if __name__ =='__main__':
    print(app.url_map)
    app.run()
    
```

返回值如

```
QuartMap([<QuartRule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>,
 <QuartRule '/api' (HEAD, GET) -> my_microservice>])
 * Serving Quart app 'c2_quart_details'
 * Environment: production
 * Please use an ASGI server (e.g. Hypercorn) directly in production
 * Debug mode: False
 * Running on http://127.0.0.1:5000 (CTRL + C to quit)
[2023-02-02 14:20:49 +0800] [2958] [INFO] Running on http://127.0.0.1:5000 (CTRL + C to quit)
[2023-02-02 14:20:54 +0800] [2958] [INFO] 127.0.0.1:51924 GET / 1.1 404 207 2034
[2023-02-02 14:20:54 +0800] [2958] [INFO] 127.0.0.1:51924 GET /favicon.ico 1.1 404 207 1791
['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cached_json', '_files', '_form', '_load_form_data', '_parse_content_type', '_parsing_lock', '_send_push_promise', 'accept_charsets', 'accept_encodings', 'accept_languages', 'accept_mimetypes', 'access_control_request_headers', 'access_control_request_method', 'access_route', 'args', 'authorization', 'base_url', 'blueprint', 'blueprints', 'body', 'body_class', 'body_timeout', 'cache_control', 'charset', 'content_encoding', 'content_length', 'content_md5', 'content_type', 'cookies', 'data', 'date', 'dict_storage_class', 'encoding_errors', 'endpoint', 'files', 'form', 'form_data_parser_class', 'full_path', 'get_data', 'get_json', 'headers', 'host', 'host_url', 'http_version', 'if_match', 'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since', 'is_json', 'is_secure', 'json', 'json_module', 'list_storage_class', 'lock_class', 'make_form_data_parser', 'max_content_length', 'max_forwards', 'method', 'mimetype', 'mimetype_params', 'on_json_loading_failed', 'origin', 'parameter_storage_class', 'path', 'pragma', 'query_string', 'range', 'referrer', 'remote_addr', 'root_path', 'root_url', 'routing_exception', 'scheme', 'scope', 'script_root', 'send_push_promise', 'server', 'stream', 'trusted_hosts', 'url', 'url_charset', 'url_root', 'url_rule', 'user_agent', 'user_agent_class', 'values', 'view_args']
<Response [200 OK]>
b'{"hello":"world"}'
[2023-02-02 14:20:59 +0800] [2958] [INFO] 127.0.0.1:51924 GET /api 1.1 200 17 1971
```

Let's explore what's happening here:

- Routing: When the service starts, Quart creates the QuartMap object, and we can see here what it knows about endpoints and the associated views.

- Request: Quart creates a Request object and my_microservice is showing us that it is a GET request to /api.

- dir() shows us which methods and variables are in a class, such as get_data() to retrieve any data that was sent with the request.

- Response: A Response object to be sent back to the client; in this case, curl. It has an HTTP response code of 200, indicating that everything is fine, and its data is the 'Hello world' dictionary we told it to send.

  

#### Routing 路徑

Routing happens in app.url_map, which is an instance of the QuartMap class that uses a library called Werkzeug.

路由發生在app.url_map中，它是QuartMap類的一個實例，使用一個名為Werkzeug的庫。

That class usees regular expressions to determine a function to decorated by @app.route matches all the incoming request.

這個類別使用常規的表達去決定路徑映射的函數



By default,the mapper will only accept GET,OPTIONS and HEAD methods on a declared route.

mapper只接受GET，OPTION，HEAD在指定的路徑。



##### Variables and converters 變量和轉換

A common requirements for an API is the ability to specify exactly which data we want to request,

API常見的功能是知道我們發送請求的代碼是哪一個。



do this with variable in the route  and allow your to describe endpoints with dynamic values 

把變量放在路徑中，並且允許多種url結束符號

```python
@app.route('/person/<person_id>')
def person(person_id):
    return {'hello':person_id}
```

還可以指定變量的類型

```python
@app.route('/price/<float:money>')
def price(money):
    return 'money is'+str(money)+"$"
```

The best practice for routing is to keep it as static and straightforward as possible.

使用路徑的最好練習是，使用靜態變量並且變量是直接的



##### The url_for function url_函數

, it will return its actual URL. Here's an example of using Python interactively

```python
from quart import url_for 
import asyncio
from c2_quart_convert import app 

async def run_url_for():
    async with app.test_request_context('/',method='GET'):
        print(url_for('person',name='Alice'))

loop = asyncio.get_event_loop()
loop.run_until_complete(run_url_for())

```





#### Request請求

When a request comes in,Quats calls the view and uses a Request Context to make sure that each request has an isolated enviroment,specific to that request,

當請求進入時，Quats調用視圖並使用請求上下文來確保每個請求都有一個特定於該請求的獨立環境，

In the following example ,an HTTP Basic Authentication request that is sent by the client is always converte to a base64 form when sent to the server.

```python
from quart import Quart,request
app = Quart(__name__)

@app.route("/")
def auth():
    print("Quart's Authorization information")
    print(request.authorization)
    return ""

if __name__ =="__main__":
    app.run()
    
```



#### Response相應

In many of the previous examples, we have simply returned a Python dictionary and left Quart to produce a response for us that the client will understand. Sometimes, we have called jsonify() to ensure that the result is a JSON object.

在前面的許多示例中，我們只是返回了一個Python字典，然後讓Quart為我們生成一個用戶端可以理解的響應。 有時，我們調用了jsonify（）來確保結果是JSON對象。

有很多其他方式做響應，we could return any of the following and Quart would bo the right thing 

- Response:create a Response object manually

  

- str:A string wil be encoded as a text/html object in the response.This is especially useful fot HTML pages

  

- dict: A dictionary wil be encoded as appliaction/json using jsonify() 

- A genrator or asynchronous generator object can be returned so that data can be streamed to the client 

- A (response,status) tuple: The response will be converted to a response object if it matches one of the preceding data types,and the status will be the HTTP response code used 

- A(response,status,headers) tuple: The response wil be converted and the response object will use a dictionary provided as headers that should be added to the response 

  

  

Here's an example with YAML, another popular way of representing data: the yamlify() function will return a (response, status, headers) tuple, which will be converted by Quart into a proper Response object:

下麵是YAML的一個示例，這是另一種流行的數據表示管道：yamlify（）函數將返回一個（response，status，headers）元組，Quart將其轉換為一個適當的response對象：

```python
from quart import Quart 
import yaml 
app = Quart(__name__)

def yamlify(data,status=200,headers=None):
    _headers = {"Content-Type":'application/x-yaml'}
    if headers is not None:
        _headers.update(headers)
    return yaml.safe_dump(data),status,_headers

@app.route('/api')
def my_microservice():
    return yamlify(['HEllO','YAML','World!'])

if __name__=='__main__':
    app.run()
    

```

上述代碼完成了

1. When the application starts,any function decorated with @app.route() is registered as view and stored in app.url_map 當應用程序啟動時，任何用@app.route（）修飾的函數都會注册為視圖並存儲在app.url_map中
2. A call is dispatched to the right view depending on its endpoint and methdo 調用將根據其端點和方法分派到正確的視圖
3. A request object is created in a local,isolated execution context 請求對象是在本地、隔離的執行上下文中創建的
4. A response object wraps the content to send back響應對象包裝要發送回的內容



### Quart's built-in featuresQuart的內寘功能

除了上述的功能，Quart還有很多其他功能是有用的

- The session object: Cookie-based data

  基于cookie的数据

   

- Globals: Storing data in the request context 

  存儲數據在請求文本中

- Signals:Sending and intercepting events 

  發送和暫停事件 

  

- Extensions and middleware : Adding features 

  擴展和中間件：添加特徵

  

- Templates: Building text-based content 

  模板：建立基於文本的內容

- Configuring:Grouping your running options in a config file 

  配置：在配置文件中集群運行選擇

  

- Blueprints:Organizing your code in namespaces 

  藍圖，組織你的代碼在命令空間

  

- Error handing and debugigng: Dealing with errors in your app 

  控制錯誤和調試，在你的web application中解決錯誤
  
  
  
  

#### Session

it's a dict-like object,which Quart serializes into a cookie on the usersiede.

這是一個類似於dict的對象，Quart將其序列化為使用者介面上的cookie。

The data contained in the session mapping is dumped into a JSON mapping ,then compressed using zlib to make it smaller and finally encoded in base64 

會話映射中包含的數據被轉儲到JSON映射中，然後使用zlib進行壓縮以使其更小，最後用base64進行編碼

When the session gets serialized the itsdangerous library signs the content using a secret_key value defined in the application

當會話被序列化時，它的危險庫使用application中定義的secret_key值對內容進行簽名

This signature, which is added to the data as a suffix, ensures that the client cannot tamper with the data that is stored in a cookie unless they know the secret key to sign the session value

此簽名作為尾碼添加到數據中，確保用戶端不會篡改存儲在cookie中的數據，除非他們知道用於簽名會話值的金鑰



However, when you're building microservices that are not producing HTML, you rarely rely on cookies as they are specific to web browsers.

然而，當您構建不生成HTML的微服務時，您很少依賴cookie，因為它們是特定於web瀏覽器的。

However,the idea of keeping a.volatile key-value storage for each user can be extremely useful for speeding up some of these server-side work .

然而，為每個用戶保留vatile鍵值存儲的想法對於加快某些伺服器端工作非常有用。





#### Globals

Quarts provides a mechanism for storing global variables that are unique to a particular request context,that i<u>s used for request and session,but is also avaible to store any custom object</u> 

適用於請求，session和存儲自定義的對象 

> It's a typical pattern in Quart to use before_request to set values in the globals. That way, all the functions that are called within the request context can interact with the special global variable called g and get the data. In the following example, we copy the username provided when the client performs an HTTP Basic Authentication in the user attribute:



```python
from quart import Quart,g,request 
app = Quart(__name__)

@app.before_request
def auth():
    if request.authorization:
        g.user = request.authorization['username']
    else:
        g.user = 'Anonymous'

@app.route("/api")
def my_microservice():
    return {"hello":g.user}

if __name__ =='__main__':
    app.run(debug=True)
```



#### Signals

Sometimes in an application, we want to send a message from one place to another, when components are not directly connected. One way in which we can send such messages is to use signals.

傳輸數據並不是直接傳輸的



Registering to a particular event is done by calling the signal's connect method,Signals are triggered when someone calls the signal's send method The send method accepts extra arguments to pass data to all the registered functions

 通過調用訊號的connect方法來注册特定事件。當有人調用訊號的send方法時，會觸發訊號。send方法接受額外的參數，將數據傳遞給所有注册的函數

```python
from quart import Quart,g,request_finished
from quart.signals import signals_available

app = Quart(__name__)
def finished(sender,response,**extra):
    print("About to send a Response")
    print(response)

request_finished.connect(finished)
@app.route("/api")
async def my_microservice():
    return {"hello":"world"}

if __name__=='__main__':
    app.run(debug=True)
    
```





#### Extensions and middleware 

Quart extensions are simply Python project that,once installed ,provide a package or a module named quart_something .They can be userful for avoiding having to reinvent anything when wanting to do things such as authentication or sending an email

Quart擴展是一個簡單的Python項目，一旦安裝，它就提供一個名為Quart_something的包或模塊。當需要進行身份驗證或發送電子郵件等操作時，Quart擴展可以使用戶無需重新設計任何東西

> to import Flask's login extension,use the following commands

```python
import quart.flask_patch 
import flask_login
```



```python
# 包錯
#AttributeError: 'list' object has no attribute 'raw_items'
from quart import Quart, request
from werkzeug.datastructures import Headers


class XFFMiddleware(object):
    def __init__(self, app, real_ip="10.1.1.1"):
        self.app = app
        self.real_ip = real_ip

    async def __call__(self, scope, receive, send):
        if "headers" in scope and "HTTP_X_FORWARDED_FOR" not in scope["headers"]:
            new_headers = scope["headers"].raw_items() + [
                (
                    b"X-Forwarded-For",
                    f"{self.real_ip}, 10.3.4.5, 127.0.0.1".encode(),
                )
            ]
            scope["headers"] = Headers(new_headers)
        return await self.app(scope, receive, send)


app = Quart(__name__)
app.asgi_app = XFFMiddleware(app.asgi_app)


@app.route("/api")
def my_microservice():
    if "X-Forwarded-For" in request.headers:
        ips = [ip.strip() for ip in request.headers["X-Forwarded-For"].split(",")]
        ip = ips[0]
    else:
        ip = request.remote_addr

    return {"Hello": ip}


if __name__ == "__main__":
    app.run()
```



#### Templates 

Jinja模板來發送郵件等歡迎界面

```python
from datetime import datetime
from jinja2 import Template
from email.utils import format_datetime
import time 
def render_email(**data):
    with open("email_template.j2") as f:
        template = Template(f.read())
    return template.render(**data)


data = {
    # 'data':time.time(),# 不顯示why
    'to':"danyow@danyow.com",
    'from':'danyowChan',
    'subject':'shopping',
    'name':'ac', 
    'items':[
        {"name":'a','price':1},
        {"name":'a','price':1},
        {"name":'a','price':1},
    ],
}
print(render_email(**data))

```



#### Configuration

Quart uses a mechanism similar to Django in its configuration approach. The Quart object comes with an object called config, which contains some built-in variables, and which can be updated when you start your Quart app via your configuration objects. For example, you can define a Config class in a Python-format file as follows:

Quart在其配寘方法中使用了類似Django的機制。 Quart對象附帶一個名為config的對象，其中包含一些內寘變數，可以在您通過配寘對象啟動Quart應用程序時進行更新。 例如，可以在Python格式檔案中定義Config類，如下所示：

```python
class Config:
    DEBUG = False 
    SQLURI  = 'postgres://username:xxx@localhost/db'

'''
可以添加到代碼中
from quart import Quart
>>> import pprint
>>> pp = pprint.PrettyPrinter(indent=4)
>>> app = Quart(__name__)
>>> app.config.from_object('prod_settings.Config') >>> pp.pprint(app.config)
'''


'''
很容易添加json，yaml等配置
>>> from quart import Quart
>>> import yaml
>>> from pathlib import Path
>>> app = Quart(__name__)
>>> print(Path("prod_settings.json").read_text()) {
    "DEBUG": false,
    "SQLURI":"postgres://username:xxx@localhost/db"
}
>>> app.config.from_json("prod_settings.json") >>> app.config["SQLURI"] 'postgres://username:xxx@localhost/db'
>>> print(Path("prod_settings.yml").read_text()) ---
DEBUG: False
SQLURI: "postgres://username:xxx@localhost/db"
>>> app.config.from_file("prod_settings.yml", yaml.safe_load)
'''
```

You can give from_file a function to use to understand the data, such as yaml.safe_load, toml.load, and json.load. If you prefer the INI format with [sections] along with name = value, then many extensions exist to help, and the standard library's ConfigParser is also straightforward.



#### Blueprints

When you write microservices that have more than a single endpoint, you will end up with a number of different decorated functions—remember those are functions with a decorator above, such as @app.route. <u>The first logical step to organize your code is to have one module per endpoint,</u> 





Blueprints take this logic a step further by providing a way to group your views into namespaces, making the structure used in separate files and giving it some special framework assistance. You can create a Blueprint object that looks like a Quart app object, and then use it to arrange some views. The initialization process can then register blueprints with app.register_blueprint to make sure that all the views defined in the blueprint are part of the app. A possible implementation of the employee's blueprint could be as follows:

藍圖通過提供一種將視圖分組到名稱空間的方法，使結構在單獨的檔案中使用，並為其提供一些特殊的框架幫助，從而使這種邏輯更進一步。 您可以創建一個看起來像Quart應用程序對象的Blueprint對象，然後使用它來排列一些視圖。 然後，初始化過程可以向app.register_blueprint注册藍圖，以確保藍圖中定義的所有視圖都是應用程序的一部分。 員工藍圖的可能實施管道如下：

```python
from quart import Blueprint 
teams = Blueprint('teams',__name__)

_DEVS = ['ALICE','BOB']
_OPS = ['Charles']
_TEAMS = {1:_DEVS,2:_OPS}

@teams.route('/teams')
def get_all():
    return _TEAMS

@teams.route("/teams/<int:team_id>")
def get_team(team_id):
    return _TEAMS[team_id]

```

The main module (app.py) can then import this file, and register its blueprint with app.register_blueprint(teams). This mechanism is also interesting when you want to reuse a generic set of views in another application or several times in the same application—it's easy to imagine a situation where, for example, both the inventory management area and a sales area might want to have the same ability to look at current stock levels.

然後，主模塊（app.py）可以導入此檔案，並將其藍圖注册到app.register_blueprint（teams）。當您希望在另一個應用程序中或在同一應用程序中重複使用一組通用視圖時，這種機制也很有趣，例如， 庫存管理區域和銷售區域可能都希望具有查看當前庫存水准的相同能力。

#### Error handing 

When something goes wrong in your application, it is important to be able to control what responses the clients will receive. In HTML web apps, you usually get specific HTML pages when you encounter a 404 (Resource not found) or 5xx (Server error), and that's how Quart works out of the box. But when building microservices, you need to have more control of what should be sent back to the client—that's where custom error handlers are useful.

The other important feature is the ability to debug your code when an unexpected error occurs; Quart comes with a built-in debugger, which can be activated when your app runs in debug mode.

**<u>app.run(debug=True)</u>**



#### Custom error handler 

Producing a generic error is a safe default behavior to avoid leaking any private information to users in the body of the error. 

生成一般錯誤是一種安全的默認行為，以避免在錯誤主體中向用戶洩漏任何私人資訊。

```python
from quart import Quart
app = Quart(__name__)

@app.errorhandler(500)
def error_handling(error):
    return {"Error":str(error)},500 

@app.route("/api")
def my_microservice():
    raise TypeError('SomeException')
if __name__ =='__main__':
    app.run(debug=True)

```



```python
from quart import Quart,jsonify,abort 
from werkzeug.exceptions import HTTPException,default_exceptions

def jsonify_errors(app):
    def error_handling(error):
        if isinstance(error,HTTPException):
            result = {
                'code':error.code,
                'description':error.description,
                'message':str(error),
            }
        else:
            description = abort.mapping[error.code].description
            result = {'code':error.code,'description':description,'message':str(error)}

        resp = jsonify(result)
        resp.status_code = result['code']
        return resp 

    for code in default_exceptions.keys():
        app.register_error_handler(code,error_handling)
    return app 

app = Quart(__name__)
app = jsonify_errors(app)

@app.route('/api')
def my_microservice():
    raise TypeError('Some exception')

if __name__ =='__main__':
    app.run(debug=True)
```



### A microservice skeleton微服務框架

how to organize the code in your projects,and how to instantiate your Quart app.-> `app.run()`



The microservice project on GitHub was created for this book and is a generic Quart project that you can use to start a microservice.

The microservice project skeletioin contains the following structure

- **setup.p**y :Distutils's setup file,which is used to install and release the project
- Makefile:A makefile that contains a few useful targets to make,build and ,run the project
- **settings.yaml**:The application default settings in a YAML file 
- **requirements.txt**:The project dependencies following the pip format produced by pip freeze 
- **myservices/**:The actual package
  - `__init_.py`
  - app.py:The app module,which contains the app itself
  - views/:A directory containing the views organized in blueprints 
    - `__init__.py`:
    - home.py:The home blueprint,which serves the root endpoint
  - tests/:
    - `__init__.py`:
    - test_home.py:Tests for the home blueprint views 





# Chapter3:Coding ,Testing and Documentation:the Virtuous Cycle編碼、測試和檔案：良性迴圈

**Test-Driven Development測試驅動開發**

is an approach where you write tests alongside the code you are creating and use the tests to guide what the code should do—and to demonstrate that it works as you expect.

是一種方法，您可以在創建的程式碼旁邊編寫測試，並使用測試來指導程式碼應該做什麼，並證明它按照您的預期工作。

**Behavior-Driven Development 行為驅動發展**



is another approach that can work well in combination with TDD. Using this method, tests describe the desired behavior of the software from a higher-level point of view and are often presented in more human- friendly language是另一種可以與TDD結合使用的方法。 使用這種方法，測試從更高層次的角度描述軟件的期望行為，並且通常以更人性化的語言呈現



a good set of tests should demonstrate that the software does what we intend it to do and that it should fail in a predictable and fixable way

> That means that if you give it invalid data or a dependency it relies on has broken,the behaviour of the code is predictable



## Different kinds of tests 不同類型的測試

- Unit tests:單元測試

  these make sure a class or a function works as expected in isolation

- Functional tests:功能測試

  Verify that the microservice does what it says from the consumer's point of view,and behaves correctly,even upon receiving bad requests.

- Integration tests:集成測試

  Verify how a microservice integrates with all its network dependencies

- Load tests:負載測試

  Measure the microservice performances 

- End-to-end tests:端到端測試

  Verify that the whole system works-from initial request to final action--through all its components

  

  

### Unit tests單元測試

Unit tests are the simplest and most self-contained tests to add to a project 

單元測試是添加到項目中的最簡單、最獨立的測試



In some cases,it will be useful to mock these calls to achieve isolation.<u>Mocking means replacing a piece of code with a fake version which will return the value you need for the test,but fake the behaviour that the real code performs</u> 



Mocking comes with its own risks,problem often occurs when u update your project's dependencies,or an external service changes what it sends,and your mock are not updated reflect the new behaviors



### Functional tests功能測試

Functional tests for a microservice project are all the tests that interact with the published API by sending HTTP requests,and asserting that the HTTP response are the expected ones.

微服務專案的功能測試是通過發送HTTP請求並斷言HTTP響應是預期響應來與發佈的API互動的所有測試。



These differ from unit tests because they focus more on the behavior of a microservice, or a smaller part of a larger service.

與單元測試不同的是，功能測試更加注重於微服務的行為，或者較大微服務的小部分內容



The key part of a functional test is to investigate whether the software's behaviour meets its requirements.As a developers ,the two most important kinds of functional tests we should focus on are the following功能測試的關鍵部分是調查軟件的行為是否符合其要求。作為開發人員，我們應該關注以下兩種最重要的功能測試

- Tests that verify that the application does what it was built for 驗證應用程序執行其構建目的的測試

- Tests that ensure an abnormal behaviour that was fixed is not happening anymore 確保已修復的异常行為不再發生的測試

  

Quart includes a QuartClient class to build requests, which can be created directly from the app object using its test_client() method. The following is an example of a test against the quart_basic app we showed in *Chapter 2*, *Discovering Quart*, which sends back a JSON body on /api/:

```python
import unittest
import json 
from quart_basic import app as test_app 
class TestApp(unittest.IsolatedAsyncioTestCase):
  async def test_help(self):
    app = tested_app.test_client()
    hello = await app.get('/api')
    body = json.load(str(await hello.get_data(),'utf-8'))
    self.assertEqual(body['Hello'],"WORLD!")
if __name__ =='__main__':
  unittest.main()
```

寫一個測試c2_quart_error.py的文件







### Intergration tests::集成測試

Intergration tests are functional tests without any mocking and should be able to run on a real deployment of your application,

集成測試是功能測試，沒有任何mock，應該能够在應用程序的實際部署上運行，





### Load tests:負載測試

The goal of a load test is to understand how your service performs under stress.

負載測試的目標是瞭解您的服務在壓力下的表現。



### End-to-End tests端到端測試

each change you make in your code should include a new test or modify an existing one.



## Using pytest and tox 使用pytest和tox

使用命令

`pytest test_*`



Once you have installed tox (using the pip install tox command), it requires a configuration file called tox.ini in the root directory of your project. 

```
[tox]
envlist =py38,py39

[testenv]
deps = pytest 
	pytest-conv 
	pytest-flake8
commands = pytest --conv=quart_basic --flake8 test_*
```





## Developer documentation

balha



## Version control

Git

## Continuous Intergration and Contonuous Deployment 持續集成和控制部署

A Continuous Integration(CI) system solves this issue by listening for changes in your version control system for the right time to run the commands you decide on, and will often take care of the different environments for you. 

持續集成（CI）系統通過在正確的時間偵聽版本控制系統中的更改以運行您决定的命令來解决此問題，並且通常會為您處理不同的環境。







# Chapter 4:Designing Jeeves設計Jeeves

> In *Chapter 1*, *Understanding Microservices*, we said that the natural way to build
>  a microservices-based app is to start with a monolithic version that implements all the features, and then to split it into microservices that make the most sense.

The chapter is organized into two main sections:

- Presentation of our application and its user stories
- How Jeeves can be built as a monolithic application





## The Jeeves bot Jeeves機器人

Jeeves will be our personal assistant—a name taken from the stories of *P. G. Wodehouse*—and used for other software bots and at least one search engine.

 





## User stories用戶故事



## Monolithic design單片設計

The first thing to consider is the retrieval of data from Slack into our application. There will be a single endpoint for this, as Slack sends all its events to the URL that the application developer configures. 

### Model

For Jeeves,the database tables are :

- User:This contains information about each user,including their credentials

- Service:This is a list of the avaible services the bot can provide,and whether or not they are active 

  

- Log:A log of bat activity

Using the **SQLAlchemy**(https://www.sqlalchemy.org/) library, each table is created as a subclass of the base class provided by the module, allowing us to avoid duplicating effort and leaving the classes in our own code clean and focused on the data that we want to work with. SQLAlchemy has asynchronous interfaces that can be used to keep the performance benefits of our async application while accessing the database. To use these features, we must install both sqlalchemy and aiosqlite. 

每個錶都是作為模塊提供的基類的子類創建的，這樣我們就可以避免重複工作，讓我們自己的程式碼中的類保持乾淨，專注於我們想要處理的數據。 SQLAlchemy具有非同步介面，可用於在訪問資料庫時保持非同步應用程序的效能優勢。 要使用這些功能，我們必須同時安裝sqlalchemy和aiosqlite。



### view and template

### A human-readable view

### Siack workspace



### Taking actions 

### OAuth tokens 

### Authentication authorization

### Background tasks 





## Putting together the monolithic design

