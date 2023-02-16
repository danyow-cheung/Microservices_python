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

### Model模型

For Jeeves,the database tables are :

- User:This contains information about each user,including their credentials

- Service:This is a list of the avaible services the bot can provide,and whether or not they are active 

  

- Log:A log of bat activity

Using the **SQLAlchemy**(https://www.sqlalchemy.org/) library, each table is created as a subclass of the base class provided by the module, allowing us to avoid duplicating effort and leaving the classes in our own code clean and focused on the data that we want to work with. SQLAlchemy has asynchronous interfaces that can be used to keep the performance benefits of our async application while accessing the database. To use these features, we must install both sqlalchemy and aiosqlite. 

每個錶都是作為模塊提供的基類的子類創建的，這樣我們就可以避免重複工作，讓我們自己的程式碼中的類保持乾淨，專注於我們想要處理的數據。 SQLAlchemy具有非同步介面，可用於在訪問資料庫時保持非同步應用程序的效能優勢。 要使用這些功能，我們必須同時安裝sqlalchemy和aiosqlite。

```python
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import update

# 初始化數據庫
DATABASE_URL = 'sqlite+aiosqlite:///./test.db'
engine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=True
)

async_session = sessionmaker(engine,expire_on_commit=False,class_ = AsyncSession)
Base = declarative_base()

# data Model
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    email = Column(String)
    slack_id = Column(String)
    password = Column(String)
    config = Column(String)
    is_activate = Column(Boolean,default=True)
    is_admin = Column(Boolean,default=False)
    
    def json(self):
        return {"id":self.id,"email":self.email,'config':self.config}
    
'''data access layer(DAL)'''
class UserDAL:
    def __init__(self,db_session):
        self.db_session = db_session
    
    async def create_user(self,name,email,slack_id):
        new_user = User(name=name,email=email,slack_id=slack_id)
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user.json()
    
    async def get_all_users(self):
        query_result = await self.db_session.execute(select(User).order_by(User.id))
        return {"Users":[user.json() for user in query_result.sclars().all()]}

    async def get_user(self,user_id):
        query = select(User).where(User.id==user_id)
        query_result = await self.db_session.execute(query)
        user = query_result.one()
        return user[0].json()
    

'''With the DAL set up,we can use a feature provided by Python's own contextlib to create an asynchronous context manager'''
@asynccontxtmanager
async def user_dal():
    async with async_session() as session:
        async with session.begin():
            yield UserDAL(session)


            
```



### view and template視圖和模板

the following Quart view will allow us to view all the users in the database when the /user endpoint is queried

```python
@app.route('/users')
async def get_all_users():
  async with user_dal() as ud:
    return await ud.get_all_users()
```





### A human-readable view人類可讀視圖

The following module implements a form for the User table ,using FlaskForm as its basis

```python
import quart.flask_patch 
from flask_wtf import FlaskForm 
import wtforms as f 
from wtforms,validators import DataRequired 

class UserForm(FlaskForm):
  email = f.StringField("email",validators=[DataRequired()])
  slack_id = f.StringField("Slack ID")
  password = f.PasswordField("password")
  display = ['email',slack_id,'password']
  
```



### Slack workspace閒置工作區

Slack allows people to connect apps to a workspace



### Taking actions 

. Even without using a microservice-based design, it is far safer to create well-defined boundaries between different components.



```python
ACTION_MAP = {
  'help':show_help_text,
  'weather':fetch_weather,
  'config':user_config
}

def process_message(message,metadata):
  '''
  Decide on an action for a chat message
  Arguments:
  	message(str):		The body of the chat message 
  	metadata(dict): Data about who sent the message,the time and channel
  '''
  reply = None 
  for test,action in ACTION_MAP.items():
    if message.startswith(test):
      reply = action(message.lstrip(test),metadata)
      break 
   if reply:
    	post_to_slack(reply,metadata)
```







### OAuth tokens 

OAuth2 allows us to make an authenticated request to someone else's site.We could request read-only access to someone's Google calendar, permission to post issues to GitHub, or the ability to read information about our recorded exercises in a fitness application

OAuth2允許我們向他人的網站發出經過身份驗證的請求。我們可以請求以只讀管道訪問他人的穀歌行事曆、向GitHub發佈問題的許可權，或者在健身應用程序中讀取有關我們記錄的鍛煉的資訊

```python
import os 
import aiohttp 
from quart import Quart,request,render_template 

app = Quart(__name__)

@app.route("/")
async def welcome_page():
    client_id = os.environ['SLACK_CLIENT_ID']
    return await render_template('welcome.html',client_id=client_id)

@app.route("/slack/callback")
async def oauth2_slack_callback():
    code = request.args['code']

    client_id = os.environ['SLACK_CLIENT_ID']
    client_secret = os.environ['SLACK_CLIENT_SECRET']
    access_url = f"https://slack.com/api/oauth.v2.access?client_id={client_id}&client_secret={client_secret}&code={code}"
    async with aiohttp.ClientSession() as session:
        async with session.get(access_url) as resp:
            access_data = await resp.json()
            print(access_data)
    
    
    return await render_template('logged_in.html')
if __name__=="__main__":
    app.run(debug=True)
    
```





### Authentication and authorization身份驗證和授權

our monolithic applications is almost ready but it also requires a way to handlw authentication and authorization,Simply but 

- Authentication: is proving that you are who you claim to be 身份驗證：證明你是你自稱的人
- Authorization: is determining what actions you are permitted to perform 授權：决定允許您執行哪些操作





### Background tasks 背景測試

到目前為止，我們的應用程序具有幾個功能，這些功能可以在無需用戶互動的情况下按計畫任務運行：我們的天氣操作可以檢查天氣警報
並向他們發送消息； 行事曆動作可以在工作日開始時報告您的計畫會議； 可以製作一份已採取行動的月度報告，並通過電子郵件發送給機器人管理員。
這些是後臺任務，它們需要在HTTP請求/響應週期之外單獨運行。 大多數作業系統都有某種形式的計畫任務功能，例如Unix上的cron或Windows中的計畫任務。 這些功能可能不適合我們的應用程序，因為這意味著我們連接到了特定的平臺，而我們在理想情况下應該是平臺無關的，並且能够在容器中運行，或者如果我們的需求發生變化，可以遷移到無服務器平臺。
<u>在Python web應用程序中運行重複後臺任務的一種流行管道是使用Celery，這是一種分佈式任務隊列</u>，可以在獨立行程中執行一些工作： http://docs.celeryproject.org.





## Putting together the monolithic design綜合整體設計

we used the following extensions and libraires 

- **aiohttp**:This handles all the outgoing HTTP requests

- **SQLAlchemy**:This is used for the model 

- **Flask-WTF** and **WTForms** : These are used for all the forms 

- **Celery and RabbitMQ**: These are used for background process and period tasks 

- **quart-auth**: This is used for managing authentication and authorization

  

<img src = '../pic/c4_desgin.png'>

无论您的应用程序正在耗尽内存、网络吞吐量、CPU处理可用性或其他瓶颈，最好的解决方案是更新
该体系结构使得服务可以在许多不同的计算机上运行。这是横向扩展，也是使用微服务的好处之一。如果
一个微服务需要比一台计算机所能提供的更多的I/O吞吐量来满足其所有请求，如果它可以跨数十台或数百台计算机运行，这不是问题。





# Chapter 5:Splitting the Monolith折開單片

in the previous chapter,we  are concerntrating on adding features rather than long-term architecture,

在上一章中，我們關注的是添加功能而不是長期架構，

in this chapter,we will 

- Examine how to identify the best components to migrate to a new microservice based on code complexity and data we collect about usage 
- Show techniques for preparing and performing that migration ,as well as checking on its success 



## Identifying potential microservice 識別潜在的微服務

There are many aspects to software and what is does --network connections,reading files,querying database,and so on.



### Code complexity and maintenance代碼複雜性和維修

take a data-informed approach by using tools that assess the cyclomatic complexity of the code 

通過使用評估程式碼圈複雜度的工具，採用基於數據的方法



**Radon** is a python tool for quickly assessing code complexity





### Metrics and Monitoring 度量和監控

It is easy to think of monitoring tools as being useful to alert us when something is broken, but there are other valuable uses. 人們很容易認為監控工具是有用的，可以在某些東西損壞時提醒我們，但還有其他有用的用途。



```python
import asyncio 
from random import randint
from aioprometheus import Gauge,Registry,Summary,inprogress,render,timer 
from quart import Quart,request 

app = Quart(__name__)
app.registry  = Registry()
app.api_requests_gauge  = Gauge(
    'quart_active_requests','Number of active requests per endpoint',
)
app.request_timer = Summary(
    'request_processing_seconds','Time spend processing request'
)
app.registry.register(app.api_requests_gauge)
app.registry.register(app.request_timer)

@app.route("/")
@timer(app.request_timer,labels ={"path":"/"})
@inprogress(app.api_requests_gauge,labels={"path":"/"})
async def index_handler():
    await asyncio.sleep(0.1)
    return "index"

@app.route("/endpoint1")
@timer(app.request_timer,labels={'path':"/endpoint1"})
@inprogress(app.api_requests_gauge,labels={"path":"/endpoint1"})
async def endpoint1_handler():
    await asyncio.sleep(randint(1000,1500)/1000.0)
    return "endpoint1"

@app.route("/endpoint2")
@timer(app.request_timer,labels={'path':"/endpoint2"})
@inprogress(app.api_requests_gauge,labels={"path":"/endpoint2"})
async def endpoint2_handler():
    await asyncio.sleep(randint(2000,2500)/1000.0)
    return "endpoint2"

@app.route("/metrics")
async def handle_metrics():
    return render(app.registry,request.headers.getlist('accept'))
if __name__=="__main__":
    app.run(debug=True)



```





### Logging 



```python
import logging
from quart import Quart,request 
import structlog 
from structlog import wrap_logger 
from structlog.processors import JSONRenderer 

app = Quart(__name__)
logger = wrap_logger(
app.logger,processors = [
    structlog.processors.add_log_level,
    structlog.processors.TimeStamper(),
    JSONRenderer(indent=4,sort_keys=True),
],)
app.logger.setLevel(logging.DEBUG)

@app.route("/hello")
def hello_handler():
    logger.info("hello_handler called")
    logger.debug(f"the request was {request}")
    return {'hello':'World!'}

if __name__=='__main__':
    app.run()
    
```





## Splitting a Monolith 

an excellent first step with any approach is to return to our service-oriented architechture principles ,and define a clear interface between the future microservice and the rest of the application

任何方法的第一步都是回到面向服務的體系結構原則，並在未來的微服務和應用程序的其他部分之間定義一個清晰的介面

```python
async def process_message(message,metadata):
  '''Decide on an action for a chat message
  Arguments:
  	message(str):  The body of the chat message
  	metadata(dict): Data about who sent the message the time and channel
  '''
  reply = NOne 
  for test,action in ACTION_MAP.items():
    if message.startwith(test):
      reply = await action(message[len(test):]metadata)
  		break 
  if reply:
    post_to_slack(reply,metadata)
    
# process the weather action
async def weather_action(text,metadata):
  if text:
    location = text.strip()
  else:
    with user_dal() as ud:
      user = ud.get_user_by_slack_id(metadata['sender'])
      if user.location:
        location = user.location 
      else:
        return "i don't know where you are "
  return await fetch_weather(location)
```



irst, it's not easy to test the way in which the location is extracted from the received message. Two new specialist functions should help with that, and ensure that these are more easily tested—the text processing in extract_location only relies on its inputs, and fetch_user_location is now just a database lookup, which we can mock in testing:s

```python
async def extract_location(text):
  '''extract location information from free-form text'''
  return re.sub(r'^weather(in )?','',text)


async def fetch_user_location(slack_id):
  location = None 
  with user_dal() as ud:
    user = ud.get_user_by_slack_id(metadata[metadata['sender']])
  location = user.location
	return location 

```



The ability to generate a more complex analysis of the text to find a location within it is now easier too, as it can be done without affecting any other code. 

```python
async def process_weather_action(text,metadata):
  potential_location = await extract_location(text)
  if not potential_location:
    potential_location = await fetch_user_location(metadata['sender'])
    if pontential_location:
      await weather_action(potential_location,metadata)
    else:
      await send_response("i don't know where you are ",metadata)

async def weather_action(location,metadata):
  reply = await fetch_weather(location)
  await send_response (reply,metadata)
```



### Feature Flags

Changing a large codebase often involves multiple large patches, which in professional environments will be reviewed by peers before they are accepted and merged.

更改大型代碼庫通常涉及多個大型補丁，在專業環境中，這些補丁將在被接受和合併之前由同行審查。

```python
@app.route('/migrating_endpoint')
async def migration_example():
  if current_app.config.get('USER_NEW_WORKER'):
    return await new_worker()
  else:
    return await original_worker()
  
@app.route('/migrating_gradually')
async def migrating_gradually_example():
  percentage_split = current_app.config.get('NEW_WORKER_PERCENTAGE')
  if percentage_split and random.randint(1,100)<=percentage_split:
    return await new_worker()
  else:
    return await original_worker()
 
```







## Refactoring Jeeves 

## workflow 

Thankfully, we have a message queue! Instead of directly calling each step
 in sequence, we can pass a message to RabbitMQ and immediately return an appropriate status code to Slack's infrastructure





# Chapter 6:Interacting with Other Services與其他服務交互

In this chapter ,we will explore this in detail:

- How one service can call another using synchronous and asychronous libraies and how to make these calls more efficient 
- How a service can use. messages to make asynchoronous calls and communicate with other services via events 
- We will also see some techniques to test services that have network dependencies 



## **Calling other web resources**调用其他web资源

As we have seen in the previous chapters, synchronous interactions between microservices can be done via HTTP APIs using JSON payloads. This is by far the pattern most often used, because both HTTP and JSON are common standards. 

正如我們在前幾章中所看到的，微服務之間的同步互動可以通過使用JSON有效負載的HTTP API實現。 這是現時最常用的模式，因為HTTP和JSON都是通用標準。



if your web service implements an HTTP API that accepts JSON,many developer usign any programming language wil be able to use it 

 

 Most of these interfaces are also RESTful, meaning that they follow the **Representational State Transfer** (**REST**) architecture principles of being stateless—with each interaction containing all the information needed instead of relying on previous exchanges—as well as cacheable and having a well-defined interface.

這些介面中的大多數也是RESTful的，這意味著它們遵循**RepresentationalStateTransfer**（**REST**）體系結構原則，即無狀態，每個互動都包含所需的所有資訊，而不是依賴於以前的交換以及可緩存，並具有定義良好的介面。



Following a RESTful scheme is not a requirement,however and some projects implement **RemoteProcedureCall(RPC)**遠程過程調用（RPC）API 



In REST, the focus is on the resource, and actions are defined by HTTP methods. 





Sending and receiving JSON payloads is the simplest way for a microservice to interact with others, and only requires microservices to know the entry points and parameters to pass using HTTP requests.發送和接收JSON有效載荷是微服務與其他服務互動的最簡單管道，並且只需要微服務知道使用HTTP請求傳遞的入口點和參數。



```python
import asyncio 
import aiohttp 

async def make_request(url):
    headers = {
        'Content-Type':'application/json',
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            print(await response.text())
url = 'http://localhost:5000/api'
loop = asyncio.get_event_loop()
loop.run_until_complete(make_request(url))

```

Since the most common way to request a semaphore is inside a with block, this means that as soon as the context of the with block is over, the semaphore is released—inside the semaphore object's __exit__ function:

由於請求信號量最常見的管道是在with塊內，這意味著只要with塊的上下文結束，信號量就會在信號量對象的__exit_函數內釋放：

```python
import asyncio 
import aiohttp 

async def make_request(url,session,semaphore):
    async with semaphore,session.get(url) as response:
        print(f'Fetching {url}')
        await asyncio.sleep(1)
        return await response.text()

async def organise_requests(url_list):
    semaphore = asyncio.Semaphore(3)
    task = list()

    async with aiohttp.ClientSession() as session:
        for url in url_list:
            task.append(make_request(url,session,semaphore))
        await asyncio.gather(*task)


urls = [
    "https://www.google.com",
    "https://developer.mozilla.org/en-US/",
    "https://www.packtpub.com/",
    "https://aws.amazon.com/",
]

loop = asyncio.get_event_loop()
loop.run_until_complete(organise_requests(urls))

```





## Finding out where to go 找到要去的地方

We want to pass in data about which URLs to use as configuration to our application. There are several options to manage more configuration options without adding them directly to the code, such as environment variables and service discovery.

我們希望將關於哪些URL用作配寘的數據傳遞給我們的應用程序。 有幾個選項可以管理更多的配置選項，而無需將它們直接添加到程式碼中，例如環境變數和服務發現。



### Environment variables 环境变量

Container-based environments are common these days, and we will discuss them in more detail in Chapter 10, Deploying on AWS. The most common approach to get configuration options into a container is to pass the container some environment variables. This has the advantage of being straightforward, since the code just needs to examine the environment when processing its configuration:

基於容器的環境現在很常見，我們將在第10章“在AWS上部署”中更詳細地討論它們。 向容器中獲取配置選項的最常見方法是向容器傳遞一些環境變數。 這具有簡單明瞭的優點，因為程式碼在處理其配寘時只需要檢查環境：

```python
import os 
def create_app(name=__name__,blueprints=None,settings=None):
  app = Quart(name)
  app.config['REMOTE_URL'] = os.environ.get('OTHER_SERVICE_URL','https://default.url/here')
  
  
```





### Service discovery 服务发现

But what if we did not need to tell our service about all its options when we deploy it? Service discovery is an approach that involves configuring an application with just a few pieces of information: where to ask for configuration and how to identify the right questions to ask.

 但是，如果我們在部署服務時不需要告訴服務它的所有選項呢？ 服務發現是一種方法，它只需要使用幾條資訊來配寘應用程序：在何處請求配寘以及如何確定要問的正確問題。





## Transfering data 传输数据

JSON is a human-readable data format. 



### HTTP cache headers HTTP缓存头

In the HTTP protocol, there are a few cache mechanisms that can be used to indicate to a client that a page that it's trying to fetch has not changed since its last visit. Caching is something we can do in our microservices on all the read-only API endpoints, such as GETs and HEADs.

The simplest way to implement it is to return, along with a result, an ETag header
 in the response. An ETag value is a string that can be considered as a version for the resource the client is trying to get. It can be a timestamp, an incremental version, or a hash. It's up to the server to decide what to put in it, but the idea is that it should be unique to the value of the response.

Like web browsers, when the client fetches a response that contains such a header, it can build a local dictionary cache that stores the response bodies and ETags as its values, and the URLs as its keys.

在HTTP協議中，有一些緩存機制可用於向用戶端訓示其嘗試獲取的頁面自上次訪問以來沒有發生變化。 緩存是我們可以在所有只讀API端點（如GET和HEAD）上的微服務中實現的。
實現它的最簡單方法是返回一個ETag頭和一個結果
在回應中。 ETag值是一個字串，可以被視為用戶端試圖獲取的資源的版本。 它可以是時間戳記、增量版本或雜湊。 由服務器决定在其中放入什麼，但其思想是，響應的值應該是唯一的。
與web瀏覽器一樣，當用戶端獲取包含此類標頭的響應時，它可以構建一個本地字典緩存，將響應體和ETag存儲為其值，將URL存儲為其關鍵字。

 

### GZIP compression GZIP压缩

Compression is an overarching term of reducing the size of data in such a way that the original data can be recovered.

压缩是一个总括性的术语，指以一种可以恢复原始数据的方式减少数据的大小。



解压缩数据会增加一些处理，但Python的GZIP模块依赖于zlib (http://www.zlib.net/)，它非常快。为了接受对HTTP查询的压缩响应，我们只需要添加一个头，表明我们可以处理gzip编码的响应:

```python
import asyncio 
import aiohttp

async def make_request():
  url = 'http://127.0.0.1/api'
  headers = {'Accept-Encoding':'gzip'}
  async with aiohttp.ClientSession(headers=headers) as session:
    async with session.get(url) as response:
      print(await response.text)
loop = asyncio.get_event_loop()
loop.run_until_complete(make_request())
```

为了压缩你发送到服务器的数据，你可以使用gzip模块并指定一个Content-Encoding头:

```python
import asyncio 
import aiohttp
import gzip 
import json 

async def make_request():
  url = 'http://127.0.0.1/api'
  headers = {'Content-Encoding':'gzip'}
  
  data = {'hello':'world','result':'ok'}
  data = bytes(json.dumps(data),'utf8')
  data = gzip.compress(data)
  
  
  async with aiohttp.ClientSession(headers=headers) as session:
    async with session.post(url,data=data) as response:
      print(await response.text())
      
loop = asyncio.get_event_loop()
loop.run_until_complete(make_request())
```





### Protocol buffers 协议缓冲区

While it is usually not relevant, if your microservice deals with a lot of data, using an alternative format can be an attractive option to increase performance, and decrease the required network bandwidth without having to use extra processing power and time compressing and decompressing the data. Two widely used binary formats are **Protocol Buffers** [protobuf](https://developers.google.com/protocol-buffers) and **MessagePack**.

虽然这通常无关紧要，但如果您的微服务要处理大量数据，使用替代格式可能是一个有吸引力的选择，可以提高性能，并减少所需的网络带宽，而不必使用额外的处理能力和时间来压缩和解压数据。两种广泛使用的二进制格式是**Protocol Buffers** [protobuf](https://developers.google.com/protocol-buffers)和**MessagePack**。



Protocol Buffers requires you to describe data that's being exchanged into some schema that will be used to index the binary content. The schemas add some work because all data that is transferred will need to be described in a schema, and you will need to learn a new **Domain-Specific Language** (**DSL**). In a typed language, such as Rust, C++, or Go, defining these structures is something that already has to be done, so the overhead is far less.

Protocol Buffers要求您描述交换到某个模式中的数据，该模式将用于索引二进制内容。模式增加了一些工作，因为传输的所有数据都需要在模式中描述，并且您需要学习一种新的领域特定语言(DSL)。在类型化语言(如Rust、c++或Go)中，定义这些结构已经是必须要做的事情，因此开销要小得多。





### MessagePack

Unlike Protocol Buffers, MessagePack (http://msgpack.org/) is schemaless, and can serialize your data by just calling a function. It's a simple alternative to JSON, and has implementations in most languages. The msgpack Python library (installed using the pip install msgpack-python command) offers the same level of integration as JSON:

与协议缓冲区不同，MessagePack (http://msgpack.org/)是无模式的，可以通过调用函数来序列化数据。它是JSON的简单替代品，在大多数语言中都有实现。msgpack Python库(使用pip install msgpack- Python命令安装)提供了与JSON相同级别的集成:

```python
import msgpack
data ={'this':'is','some':'data'}
msgpack.pack(data,use_bin_type=True)
msgpack.pack(msgpack.packb(data,use_bin_type=True))
```





### Putting it together 

before moving on ,we will quickly recall what we have covered so far:

- Implementing HTTP cahce headers is a great way to speed up repeated requests for data 
- GZIP compression is an efficient way to lessen the size of requests and responses and is easy to set up 
- Binary protocols are an attractive alternative to plain JSON,but it does depend on the situation



## Asynchronous messages 异步消息

在微服务体系结构中，当过去在单个应用程序中执行的流程现在涉及多个微服务时，异步调用起着基本作用。在前一章中，我们通过对Jeeves应用程序的更改简要地谈到了这一点，现在它使用异步消息队列与其工作者通信。为了更好地利用这些工具，我们将更深入地研究这些工具。



异步调用可以像微服务应用程序中的一个单独的线程或进程一样简单，它正在接收一些要完成的工作，并在不干扰同时发生的HTTP请求/响应往返的情况下执行它。
但是直接从相同的Python进程执行所有操作不是很健壮。如果进程崩溃并重新启动，会发生什么?如果后台任务是这样构建的，我们如何扩展后台任务呢?



发送由另一个程序选择的消息更可靠，并让微服务专注于其主要目标，即为客户端提供响应。如果web请求不需要立即回答，那么我们服务中的端点可以变成代码，接受HTTP请求，处理它，并传递它，它对客户端的响应现在是我们的服务是否成功接收到请求，而不是请求是否被处理。



在前一章中，我们研究了如何使用Celery来构建一个微服务，它可以从像RabbitMQ这样的消息代理那里获得一些工作。在这种设计中，芹菜工作线程阻塞——也就是说，它在等待时停止操作——直到新消息添加到RabbitMQ队列中。



### Message queue reliability 消息队列可靠性

we would like to add a message to the queue and have it delivered—and acted upon—exactly once. In practice this is almost impossible to achieve in a distributed system, as components fail, experiencing high latency or packet loss, while all sorts of complex interactions occur.

我们希望将一条消息添加到队列中，并将其交付(并执行)一次。实际上，这在分布式系统中几乎是不可能实现的，因为在各种复杂的交互发生时，组件会出现故障，经历高延迟或包丢失。



we have two real choices,encoded in RabbitMQ's delivery strategies 'at-most-once' and 'at-least-once'

我们有两个真正的选择，在RabbitMQ的交付策略中编码为'at-most-once'和'at-least-once'



最多交付一次消息的策略不会解释消息交付系统中的任何不可靠性或工作人员中的故障。一旦工作人员接受了消息，消息队列就会忘记它。如果工人随后遭遇失败，没有完成分配给他的大块工作，这是更广泛的系统需要处理的问题。

有了至少一次传递消息的承诺，在任何失败的情况下，传递将再次尝试，直到一个工作者接受消息并承认它已经对它进行了操作。这确保了没有数据丢失，但这确实意味着在某些情况下，消息可以传递给多个工作人员，因此某种通用唯一标识符(UUID)是一个好主意，这样虽然某些工作可能会重复，但当将其写入任何数据库或存储时，它可以被重复删除。关于分布式系统可靠性和像PAXOS这样的共识协议的更广泛的讨论将需要一本书。





### Basic queues 基本隊列

One service pushes messages into a specific queue,and some workers pick them up from the other end and perform an action on them,



<img src ='../pic/basic_queue.png'>



没有双向通信—发送方只是在队列中存放消息并离开。下一个可用的工作人员将获得下一个消息。当您想要执行一些异步并行任务时，这种盲目的单向消息传递非常完美，这使得它易于扩展。
此外，一旦发送方确认消息已添加到代理，我们就可以让消息代理(如rabbitmq)提供一些消息持久性。换句话说，如果所有工作线程都脱机，我们不会丢失队列中的消息。



### Topic exchanges and queues 主题交换和队列

主题是一种过滤和分类在队列中传递的消息的方法。当使用主题时，发送的每条消息都带有一个额外的标签，帮助识别它是什么类型的消息，我们的员工可以订阅特定的主题，或者匹配几个主题的模式。



```python
from pika import BlockingConnection,BasicProperties

def message(topic,message):
  connection = BlockingConnection()
  try:
    channel = connection.channel()
    props = BasicProperties(content-type='text/plain',delivery_mode=1)
    channel.basic_publish('incoming',topic,message,props)
  finally:
    connection.close()

message("publish.playstore", "We are publishing an Android App!")
message("publish.newsletter", "We are publishing a newsletter!")

```







### Publish/subscribe 

pass 



## Testing 



```python
import asyncio
import aiohttp 

import pytest 
from aioresponses import aioresponses 

@pytest.fixture
def mock_aioresponse():
    with aioresponses() as m:
        yield m 

@pytest.mark.asyncio
async def test_ctx(mock_aioresponse):
    async with aiohttp.ClientSession() as session:
        mock_aioresponse.get("http://test.example.com", payload={"foo":
"bar"})
        resp = await session.get("http://test.example.com")
        data = await resp.json()
    assert {"foo": "bar"} == data
```

In this example, we tell aioresponses that any GET request made to http://test. example.com should return the data we specify. This way we can easily provide mocked responses for several URLs, and even the same URL by invoking mocked.get more than once to create multiple responses for the same endpoint.

在本例中，我们告诉aioresponses任何GET请求都发送到http://test。Example.com应该返回我们指定的数据。通过这种方式，我们可以轻松地为多个URL提供模拟响应，甚至通过调用被模拟的URL提供相同的响应。获取多个信息，为同一个端点创建多个响应。



## Using OpenAPI 



The OpenAPI Specification (https://www.openapis.org/), previously known as Swagger, is a standard way of describing a set of HTTP endpoints, how they are used, and the structure of the data that is sent and received. By describing an API using a JSON or YAML file, it allows the intent to become machine-readable—this means that with an OpenAPI Specification, you can use a code generator to produce a client library in a language of your choosing, or to automatically validate data as it enters or leaves the system.

OpenAPI has the same goal that WSDL (https://www.w3.org/TR/2001/NOTE- wsdl-20010315) had back in the XML web services era, but it's much lighter and straight to the point.

The following example is a minimal OpenAPI description file that defines one single /apis/users_ids endpoint and supports the GET method to retrieve the list of user IDs:



OpenAPI规范(https://www.openapis.org/)，以前称为Swagger，是描述一组HTTP端点、如何使用它们以及发送和接收的数据结构的标准方法。通过使用JSON或YAML文件描述API，它允许意图变成机器可读——这意味着使用OpenAPI规范，您可以使用代码生成器以您选择的语言生成客户端库，或者在数据进入或离开系统时自动验证数据。
OpenAPI的目标与WSDL (https://www.w3.org/TR/2001/NOTE- WSDL -20010315)在XML web服务时代的目标是一样的，但是它更简单，更直奔主题。
下面的例子是一个最小的OpenAPI描述文件，它定义了一个单一的/apis/users_ids端点，并支持GET方法来检索用户id列表:





# Chapter 7: Securing your service 保障你的服務



## The OAuth2 protocol



The potential for security leaks multiplies with the number of different places an identity is stored, and how many routes a password can
 take through the different systems involved.

安全泄漏的可能性随着身份存储的不同位置的数量以及密码可以通过的路由的数量而增加
仔细研究所涉及的不同系统。





OAuth2 is a standard that is widely adopted for securing web applications and their interactions with users and other web applications.

OAuth2是一个被广泛采用的标准，用于保护web应用程序及其与用户和其他web应用程序的交互。

<img src= '../pic/OAuth2.png'>







## X.509 certificate-based authenitication

The X.509 standard (https://datatracker.ietf.org/doc/html/rfc5280) is used to secure the web. Every website using TLS—the ones with https:// URLs—has an X.509 certificate on its web server, and uses it to verify the server's identity and set up the encryption the connection will use.

X.509标准(https://datatracker.ietf.org/doc/html/rfc5280)用于保护网络。每个使用tls的网站——那些带有https:// url的网站——在其web服务器上都有一个X.509证书，并使用它来验证服务器的身份并设置连接将使用的加密。



## Token-based authentication

正如我们前面所说的，当一个服务希望在没有任何用户干预的情况下访问另一个服务时，我们可以使用CCG流。CCG背后的思想是，服务可以连接到身份验证服务并请求令牌，然后它可以使用令牌对其他服务进行身份验证。



a token is usually built as a complete proof that you have permission to use a service,It is complete because it is possible to validate the token with the authentications service without knowing anything else.or having to query an external resource. Depending on the implementation, a token can also be used to access different microservices.

令牌通常被构建为您拥有使用服务权限的完整证明，它是完整的，因为可以在不知道其他任何事情的情况下使用身份验证服务验证令牌。或者必须查询外部资源。根据实现的不同，令牌还可以用于访问不同的微服务。



OAuth2 uses the JWT standard for its tokens,There is nothing in OAuth2 that requires the use of JWT -it just  happens to be a good fit for what OAuth2 wants to do.OAuth2使用JWT标准作为它的令牌，OAuth2中没有任何东西需要使用JWT——它恰好很适合OAuth2想要做的事情。



### The JWT standard 

JWT = Json Web Token 

A JWT is a long string composed of three dot-separated parts:JWT是由三个点分隔的部分组成的长字符串:

- A header:这提供了关于令牌的信息，例如使用哪种散列算法

  

- A playload:这是实际数据

  

- A signature:这是头和有效负载的带符号散列，用于验证它是否合法

Each part in the token above is separated by a line break for display purposes—the original token is a single line. You can experiment with JWT encoding and decoding using a utility provided by Auth0 at https://jwt.io/.

出于显示的目的，上面标记中的每个部分都由换行符分隔——原始标记是一行。您可以使用Auth0在https://jwt.io/上提供的实用程序来试验JWT编码和解码。

```python
import base64 
def decode(data):
  # adding extra = for padding if needed 
  pad = len(data)%4 
  if pad>0:
    data += '='*(4-pad)
  return base64.urlsafe_b64decode(data)

decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
# b'{"alg":"HS256","typ":"JWT"}'
```



These headers give us a lot of flexibility to control how long our tokens will stay valid. Depending on the nature of the microservice, the token **Time-To-Live** (**TTL**) can be anything from very short to infinite.



### PyJWT 

In Python, the PyJWT library provides all the tools you need to generate and read back JWTs: 

一旦pip安装了pyjwt(和密码学)，就可以使用encode()和decode()函数来创建令牌。在下面的例子中，我们将使用HMAC-SHA256创建一个JWT并读取它。当读取令牌时，通过提供秘密来验证签名:

```python
import jwt 
def create_token(alg='HS256',secret='secret',data=None):
  return jwt.encode(data,secret,algorithm=alg)

def read_token(token,secret='secret',algs=['HS256']):
  return jwt.decode(token,secret,algorithms=algs)

token = create_token(data={'some':'data',"inthe":'token'})
print(token)
print(read_token(token))
```







### Using a certificate with JWT 使用带有JWT的证书

To simplify matters for this example, we will use the letsencrypt certificates we generated for nginx earlier on. If you are developing on a laptop or container that is not available from the internet, you may need to generate those certificates using a cloud instance or a certbot DNS plugin and copy them to the right place.为了简化这个例子，我们将使用之前为nginx生成的letsencrypt证书。如果你是在笔记本电脑或容器上进行开发，那么你可能需要使用云实例或certbot DNS插件生成这些证书，并将它们复制到正确的位置。

If certbot generated the certificates directly, they will be available in /etc/ letsencrypt/live/your-domain/. To start with, we are interested in these two files:

- cert.pem, which contains the certificate

- privkey.pem, which has the RSA private key

  In order to use these with PyJWT, we need to extract the public key from the certificate:

  ```
    openssl x509 -pubkey -noout -in cert.pem  > pubkey.pem
  ```



**RSA** stands for **Rivest, Shamir, and Adleman**, the three authors. The RSA encryption algorithm generates crypto keys that can go up to 4,096 bytes, and are considered secure.

From there, we can use pubkey.pem and privkey.pem in our PyJWT script to sign and verify the signature of the token, using the RSASSA-PKCS1-v1_5 signature algorithm and the SHA-512 hash algorithm:

**RSA**代表**Rivest, Shamir和Adleman**，三位作者。RSA加密算法生成的加密密钥最大可达4096字节，被认为是安全的。

从那里，我们可以使用pubkey。Pem和privkey。在PyJWT脚本中使用RSASSA-PKCS1-v1_5签名算法和SHA-512哈希算法来签名和验证令牌的签名:

```python
import jwt 
with open('pubkey.pem')as f:
  PUBKEY = f.read()
  
with open('privkey.pem') as f:
  PRIVKEY = f.read()

def create_token(**data):
  return jwt.encode(data,PRIVKEY,algorithm='RSS512')

def read_token(token):
  return jwt.decode(token,PUBKEY,algorithms='RS512')

token = create_token(some='data',inthe='token')
print(token)

read = read_token(token)
print(read)
```



## The TokenDealer microservice

Our first step in building the authentication microservice will be to implement everything needed to perform a CCG flow.

构建身份验证微服务的第一步是实现执行CCG流所需的一切。

为此，应用程序接收来自需要令牌的服务的请求，并根据需要生成它们，假设请求中有一个已知的秘密。生成的令牌的生命周期为一天。这种方法具有最大的灵活性，没有生成我们自己的X.509证书的复杂性，同时允许我们有一个服务负责生成令牌。



### The OAuth implementation

对于CCG流，需要令牌的服务发送带有URL编码主体的POST请求，该主体包含以下字段:

- client_id:这是标识请求者的唯一字符
- client_secret:这是一个验证请求者身份的秘密密钥。它应该是预先生成并向认证服务注册的随机字符串。
- grant_type:授权类型，这里必须是client_credentials。

令牌本身是一个包含几个字段的数据结构:令牌的发行者(iss)，通常是服务的URL;令牌的预期受众(aud)，即
是，代币是给谁用的;代币发行的时间(iat);以及它的到期(exp)时间。然后使用jwt对数据进行签名。Encode方法，并将其返回给请求客户端:

```python
@app.route('/oauth/token',methods=["POST"])
async def create_token():
  with open(current_app.config['PRIVATE_KEY_PATH']) as f:
    key = f.read().strip()
  try:
    data = await request.form 
    if data.get('grant_type')!= 'client_credentials':
      return bad_request(f"Wrong grant_type {data.get('grant_type')}")
    client_id = data.get('client_id')
    client_secret = data.get('client_secret')
    aud = data.get('audience','')
    if not is_authorized_app(client_app,client_secret):
      return abort(401)
   	now = int(time.time())
    token = {
      'iss':current_app.config['TOKENDEALER_URL'],
      'aud':aud,
      'iat':now,
      'exp':now+3600*24,
    }
    token = jwt.encode(token,key,algorithm='RSS512')
    return {'access_token':token}
  except Exception as e:
    print(e)
    return bad_request('Unable to create a token')
```



接下来要添加的视图是一个函数，该函数返回令牌生成所使用的公钥，这样任何客户端都可以验证令牌，而无需进一步发出HTTP请求。它通常位于众所周知的url中——该地址字面上包含字符串. famous /，这是IETF鼓励的一种实践，它为客户端提供了一种发现服务元数据的方法。我们用JWKS来回应。

在返回的数据中有密钥类型(kty)，算法(alg)，公钥使用(use) -这里是签名-以及RSA算法使用的两个值，我们的加密密钥是用这些值生成的:

```python
@app.route("/.well-known/jwks.json")
async def _jwks():
  '''Returns the public key in the JSON Web key Set(JWKS) format'''
  with open(current_app.config['PUBLIC_KEY_PATH']) as f:
    key = f.read().strip()
    
  data = {
        "alg": "RS512",
        "e": "AQAB",
        "n": key,
        "kty": "RSA",
        "use": "sig",
    }
  return jsonify({'keys':[data]})

```

最后一个视图允许客户端验证一个令牌，而不需要自己做这些工作。与令牌生成相比，我们简单地从输入数据中提取正确的字段，并调用jwt.decode函数来提供值。注意，这个函数验证令牌是否有效，但不验证令牌是否允许任何特定的访问——这部分取决于提供令牌的服务:

```python
@app.route('/verify_token',methods=['POST'])
async def verify_token():
  with open(current_app.config['PUBLIC_KEY_PATH']) as f:
    key = f.read()
  try:
    input_data = await request.form 
    token = input_data['access_token']
    audience = input data.get('audience','')
    return jwt.decode(token,key,algorithms=['RSS512'],audience=audience)
  except Exception as e:
    return bad_request('Unable to verify the token')
    
```









### Using TokenDealer

In jeeves,the Data service is a good example of a place where authentication is required,Adding information via the Data service needs to be restricted to authorized services 

在Jeeves中，数据服务是需要身份验证的一个很好的例子。通过数据服务添加信息需要限制为授权服务:

<img src ='../pic/token_dealer.png'>

在完整的实现中，第一步可以部分自动化。生成一个
客户端保密通常是通过身份验证服务中的web管理面板完成的。然后将该秘密提供给客户端微服务开发人员。每个需要令牌的微服务现在都可以获得一个令牌，无论是第一次连接，还是因为它已经获得的令牌已经过期。他们
使用它需要做的是在调用数据服务时将该令牌添加到授权标头。



 ```python
 _TOKEN = None
 from c7_fetch_token import get_token
 import requests
 def get_auth_header(new=False):
     global _TOKEN
     if _TOKEN is None or new:
         _TOKEN = get_token()
     return "Bearer"+_TOKEN
 
 _dataservice = 'https://localhost:5001'
 def _call_service(endpoint,token):
     # not using sessioin and other tools,to simplify the code 
     url = _dataservice +'/'+endpoint
     headers = {'Authorization':token}
     return requests.get(url,headers=headers)
 
 def call_data_service(endpoint):
     token = get_auth_header()
     response = _call_service(endpoint,token)
     if response.status_code==401:
         # the token might be revoked,let's try with a fresh one 
         token = get_auth_header(new=True)
         response = _call_service(endpoint,token)
     return response
 
 
 
 ```

如果对数据服务的调用导致401响应，call_data_service()函数将尝试获得一个新的令牌。这种401上的刷新令牌模式可用于所有微服务，以自动生成令牌。
这包括服务到服务的身份验证。您可以找到完整的实现
在示例GitHub存储库中使用这个基于jwt的身份验证方案，并将其作为构建身份验证过程的基础。
下一节将介绍保护web服务的另一个重要方面，即保护代码本身。

##  Securing your code 

Anything that is published to the web can be attacked, although we have the advantage that most microservices are not exposed to the public internet, which reduces the possible ways they could be exploited. The expected inputs and outputs of the system are narrower, and often better defined using specification tools, such as OpenAPI.

Attacks are not always due to hostile intent, either. If the caller has a bug or is just not calling your service correctly, the expected behavior should be to send back a 4xx response and explain to the client why the request was rejected.

发布到网络上的任何东西都可能被攻击，尽管我们有一个优势，即大多数微服务都没有暴露在公共互联网上，这减少了它们被利用的可能方式。系统的预期输入和输出范围更窄，通常使用规范工具(如OpenAPI)进行更好的定义。
攻击也不总是出于敌意。如果调用者有一个错误或者没有正确地调用您的服务，预期的行为应该是发送回一个4xx响应，并向客户端解释为什么请求被拒绝。



Things such as Local File Inclusion (LFI), Remote File Inclusion (RFI), or Remote Code Execution (RCE) are all attacks that trick the server into executing something via client input, or revealing server files. They can happen of course in applications written in most languages and toolkits, but we will examine some of Python's tools to protect against these attacks.
The idea behind secure code is simple, yet hard to do well in practice. The two fundamental principles are:
• Every request from the outside world should be carefully assessed before it does something in your application and data.
• Everything your application is doing on a system should have a well-defined and limited scope.
诸如本地文件包含(LFI)、远程文件包含(RFI)或远程代码执行(RCE)等都是通过客户端输入诱骗服务器执行某些内容或泄露服务器文件的攻击。当然，在用大多数语言和工具包编写的应用程序中，它们都可能发生，但我们将研究一些Python工具来防止这些攻击。
安全代码背后的思想很简单，但在实践中很难做好。这两个基本原则是:
- 来自外部世界的每个请求都应该在它对你的应用程序和数据起作用之前仔细评估。
- 应用程序在系统上所做的一切都应该有一个定义良好且有限的作用域。

### Limiting your application scope 限制应用范围



Even if you trust the authentication system, you should make sure that whoever connects has the minimum level of access required to perform their work. 

即使多信任认证系统，也要保证用户的权限是较低的。





That scope limitation can be done with JWTs by defining roles (such as read/write) and adding that information in the token under a permissions or scope key, for example. The target microservice will then be able to reject a call on a POST that is made with a token that is supposed to only read data.

jwt可以通过定义角色(例如读/写)并在权限或范围键下的令牌中添加该信息来实现范围限制。然后，目标微服务将能够拒绝对POST的调用，该调用使用的令牌应该只用于读取数据。



There are two rules you should follow:

1. All software should run with the smallest set of permissions possible 
2. Be very cautious when executing processes from your web service,and avoid it if you can 





### Untrusted incoimg data 不要信任输入数据 

大多数应用程序接受数据作为输入:查询谁的帐户;去哪个城市买天气预报;把钱转到哪个账户，等等。问题是来自我们系统之外的数据不容易被信任。
前面，我们讨论了SQL注入攻击;现在让我们考虑一个非常简单的例子，我们使用SQL查询来查找一个用户。我们有一个函数，它将查询作为一个要格式化的字符串，并使用标准Python语法填充它:

```python
import pymysql 

conn = pymysql.connect(host='localhost',db='book')

def get_user(user_id):
  query = f'select * from user where id={user_id}'
  with conn.cursor() as cursor:
    cursor.execute(query)
    result = cursor.fetchone()
    return result 
  
```

以上的代码写法会引起SQL注入的问题

get_user will perform the expected query, and a second query that will add a
 new user! It could also delete a table, or perform any other action available to SQL statements. Some damage limitation is there if the authenticated client has limited permissions, but a large amount of data could still be exposed. This scenario can be prevented by quoting any value used to build raw SQL queries. In PyMySQL, you just need to pass the values as parameters to the execute argument to avoid this problem:Get_user将执行预期的查询，第二个查询将添加一个
新用户!它还可以删除表，或执行SQL语句可用的任何其他操作。如果经过身份验证的客户端权限有限，则会有一些损害限制，但仍可能暴露大量数据。可以通过引用用于构建原始SQL查询的任何值来防止这种情况。在PyMySQL中，你只需要将值作为参数传递给execute参数来避免这个问题:

```python
def get_user(user_id):
  query = f'select * from user where id = %s'
  with conn.cursor() as cursor:
    cursor.execute(query,(user_id,))
    result = cursor.fetchone()
    return result 
```

**Server-Side Template Injection** (**SSTI**) is a possible attack in which your templates blindly execute Python statements. In 2016, such an injection vulnerability was found on Uber's website on a Jinja2 template, because raw formatting was done before the template was executed. See more at https://hackerone.com/reports/125980.

服务器端模板注入(SSTI)是一种可能的攻击，在这种攻击中，模板盲目地执行Python语句。2016年，在优步网站上的一个Jinja2模板上发现了这样一个注入漏洞，因为在模板执行之前已经完成了原始格式化。详见https://hackerone.com/reports/125980。

代码如下所示

```python
from quart import Quart,request,render_template_string 

app = Quart(__name__)

SECRET = 'oh no !'
_TEMPLATE = """Hellp %s Welcome to my API"""

class Extra:
  def __init__(self,data):
    self.data =data 
@app.route("/")
async def my_microservice():
  user_id = request.args.get('user_id','Anonymous')
  tmpl = _TEMPLATE % user_id 
  return await render_template_string(tmpl,extra=Extra('something'))

app.run()
```







### Redirecting and trusting queries 重定向和信任查询

The same precaution applies when dealing with redirects. One common mistake is to create a login view that makes the assumption that the caller will be redirected to an internal page and use a plain URL for that redirect:

```python
@app.route('/login')
def login():
  from_url = request.args.get('from_url','/')
  # do something authentication
  return redirect(from_url)
```



This can be done with the after_request() hook that will be called after our views have generated a response, but before Quart has sent it back to the client. If the application tries to send back a 302, you can check that its location is safe, given a list of domains and ports:



这可以通过after_request()钩子来实现，该钩子将在视图生成响应之后，但在Quart将响应发送回客户端之前被调用。如果应用程序试图发送回一个302，你可以检查它的位置是否安全，给出一个域和端口列表:

```python
from quart import Quart,redirect 
from quart.helpers import make_response 
from urllib.parse import urlparse

app = Quart(__name__)
@app.route('/api')
async def my_microservice():
    return redirect('https://github.com:443/')

# domain:port 
SAFE_DOMAINS = ['github.com:443','google.com:443']

@app.after_request
async def check_redirect(response):
    if response.status_code != 302:
        return response
    url = urlparse(response.location)
    netloc = url.netloc

    if netloc not in SAFE_DOMAINS:
        # not using abort() here or it'll break the hook 
        return await make_response('Forbidden',403)
    return response

if __name__=="__main__":
    app.run(debug=True)
    
```





### Sanitizing input data 消毒（過濾）输入数据

> 什么翻译，wtf

除了处理不可信数据的其他实践之外，我们可以确保
字段本身符合我们的期望。面对上面的例子，它
很容易想到我们应该过滤掉任何分号，或者可能是所有的花括号，但这让我们不得不考虑数据可能畸形的所有方式，并试图智取恶意程序员和随机错误的创造力。



<u>To summarize, you should always treat incoming data as a potential threat</u>, as a source of attacks to be injected into your system. Escape or remove any special characters, avoid using the data directly in database queries or templates without a layer of isolation between them, and ensure your data looks as you would expect it to.

There is also a way to continuously check your code for potential security issues using the Bandit linter, explored in the next section.

总而言之，您应该始终将传入的数据视为潜在威胁，将其视为注入系统的攻击源。转义或删除任何特殊字符，避免在没有隔离层的情况下直接在数据库查询或模板中使用数据，并确保数据看起来像您期望的那样。
还有一种使用Bandit linter连续检查代码的潜在安全问题的方法，这将在下一节中讨论。



### Using bandit linter 用强盗的羊绒

[Bandit](https://github.com/ PyCQA/bandit) is another tool to scan your source code for potential security risks.

t can be run in CI systems for the automatic testing of any changes before they
 get deployed.



### Dependencies依赖关系

[Dependabot](https://dependabot.com/) is a tool that will perform security sweeps of your project's dependencies. Dependabot is a built-in component of GitHub, and its reports should be visible in your project's **Security** tab. Turning on some extra features in the project's **Settings** page allows Dependabot to automatically create pull requests with any changes that need making to remain secure.

PyUp has a similar set of features but requires manually setting up—as does Dependabot if you're not using GitHub.



[Dependabot](https://dependabot.com/)是一个对项目依赖项执行安全扫描的工具。Dependabot是GitHub的内置组件，它的报告应该在项目的**Security**选项卡中可见。在项目的**Settings**页面中打开一些额外的功能，允许Dependabot自动创建拉请求，并对需要保持安全的任何更改进行更改。

PyUp有一组类似的功能，但需要手动设置——如果你不使用GitHub, Dependabot也需要手动设置。



## Web application firewall 网路应用程序的防火墙

> Even with the safest handling of data, our application can still be vulnerable to attack. When you're exposing HTTP endpoints to the world, this is always a risk. You will be hoping for callers to behave as intended, with each HTTP conversation following a scenario that you have programmed in the service.
>
> 即使对数据进行了最安全的处理，我们的应用程序仍然容易受到攻击。当您向外界公开HTTP端点时，这总是有风险的。您希望调用方的行为符合预期，每个HTTP会话都遵循您在服务中编程的场景。



A client can send legitimate requests and just hammer your service with it, leading to a **Denial of Service** (**DoS**) due to all the resources then being used to handle requests from the attacker. When many hundreds or thousands of clients are used to do this, it's known as a **Distributed Denial of Service** (**DDoS**) attack. This problem sometimes occurs within distributed systems when clients have replay features that are automatically recalling the same API. If nothing is done on the client side to throttle calls, you might end up with a service overloaded by legitimate clients.

客户端可以发送合法的请求，<u>然后用它来敲打您的服务，导致拒绝服务(DoS)</u>，因为所有的资源都被用于处理来自攻击者的请求。当数百或数千个客户端被用来这样做时，它被称为<u>分布式拒绝服务(DDoS)攻击</u>。在分布式系统中，当客户端具有自动调用相同API的重放特性时，有时会出现此问题。如果客户端没有采取任何措施限制调用，那么您可能最终会得到一个由合法客户端超载的服务。





### OpenResty:Lua and nginx 

[OpenRest](http://openresty.org/en/) is an nginx distribution that embeds a [Lua](http://www.lua.org/) interpreter that can be used to script the web server. We can then use scripts to apply rules and filters to the traffic.

Lua is an excellent, dynamically typed programming language that has a lightweight and fast interpreter. The language offers a complete set of features and has built-in async features. You can write coroutines directly in vanilla Lua.

If you install Lua (refer to http://www.lua.org/start.html), you can play with the language using the Lua **Read-Eval-Print Loop** (**REPL**), exactly as you would with Python:

[OpenRest](http://openresty.org/en/)是一个nginx发行版，它嵌入了一个[Lua](http://www.lua.org/)解释器，可以用来为web服务器编写脚本。然后，我们可以使用脚本对流量应用规则和过滤器。

Lua是一种优秀的动态类型编程语言，它有一个轻量级的快速解释器。该语言提供了一组完整的特性，并具有内置的异步特性。你可以直接用vanilla Lua编写协程。

如果你安装了Lua(参考http://www.lua.org/start.html)，你可以使用Lua **Read-Eval-Print Loop** (**REPL**)来玩这门语言，就像你使用Python一样:

On macOS, you can use Brew and the `brew install openresty` command.

Once OpenResty is installed, you will get an openresty command, which can be used exactly like nginx to serve your applications. In the following example, the nginx configuration will proxy requests to a Quart application running on port 5000:

一旦安装了OpenResty，你将得到一个OpenResty命令，它可以像nginx一样使用来为你的应用程序服务。在下面的例子中，nginx配置将把请求代理给一个运行在端口5000上的Quart应用程序:

```
# resty.conf
daemon off;
worker_processes  1;
error_log /dev/stdout info;
events {
worker_connections  1024;
}
http {
  access_log /dev/stdout;
  server {
    listen   8888;
    server_name  localhost;
    location / {
      proxy_pass http://localhost:5000;
      proxy_set_header Host $host;
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
} }
}

```





Lua can be invoked at different moments when a request comes in; the two that are most attractive to this chapter are:

- access_by_lua_block: This is called on every incoming request before a response is built, and is where we can build access rules in our WAF
- content_by_lua_block: This uses Lua to generate a response



当请求进入时，Lua可以在不同的时刻调用;本章最吸引人的两点是:

- access_by_lua_block:在构建响应之前，对每个传入的请求都调用这个函数，并且我们可以在WAF中构建访问规则
- content_by_lua_block:使用Lua生成响应



### Rate and concurrency limiting 



**Rate limiting** consists of counting how many requests a server accepts within a given period of time, and rejecting new ones when a limit is reached.

**速率限制**包括计算服务器在给定时间内接受多少请求，并在达到限制时拒绝新的请求。



**Concurrency limiting** consists of counting how many concurrent requests are being served by the web server to the same remote user, and rejecting new ones when it reaches a defined threshold. Since many requests can reach the server simultaneously, a concurrency limiter needs to have a small allowance in its threshold.



**并发限制**包括计算web服务器向同一远程用户提供的并发请求的数量，并在达到定义的阈值时拒绝新的请求。由于许多请求可以同时到达服务器，因此并发限制器的阈值需要有一个小的允许值。





In the following example, we're adding a lua_shared_dict definition and a section called access_by_lua_block to activate the rate limiting. Note that this example is a simplified version of the example in the project's documentation:

在下面的示例中，我们添加了一个lua_shared_dict定义和一个名为access_by_lua_block的节来激活速率限制。注意，这个例子是项目文档中例子的简化版本:

> copy and pasta 

```lua
# resty_limiting.conf
daemon off;
worker_processes  1;
error_log /dev/stdout info;
events {
    worker_connections  1024;
}
http {
    lua_shared_dict my_limit_req_store 100m;
server {
  listen   8888;
  server_name  localhost;
  access_log /dev/stdout;
  location / {
              access_by_lua_block {
                  local limit_req = require "resty.limit.req"
                  local lim, err = limit_req.new("my_limit_req_store",200,100)
                  local key = ngx.var.binary_remote_addr
                  local delay, err = lim:incoming(key, true)
                  if not delay then
                      if err == "rejected" then
                          return ngx.exit(503)
                      end
                      ngx.log(ngx.ERR, "failed to limit req: ", err)
                      return ngx.exit(500)
                  end
                  if delay >= 0.001 then
                      local excess = err
                      ngx.sleep(delay)
                  end
  }
  proxy_pass http://localhost:5000;
  proxy_set_header Host $host;
  proxy_set_header X-Real-IP $remote_addr;
  proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  } }
  }

```





### Other OpenResty features 

For instance, if you are using a Redis or a Memcached server to cache some of your GET resources, you can directly call them from Lua to add or fetch a cached version for a given endpoint. The srcache-nginx-module (https://github.com/openresty/ srcache-nginx-module) is an implementation of such behavior, and will reduce the number of GET calls made to your Quart apps if you can cache them.

To conclude this section about WAFs: OpenResty is a powerful nginx distribution that can be used to create a simple WAF to protect your microservices. It also offers abilities that go beyond firewalling. In fact, if you adopt OpenResty to run your microservices, it opens a whole new world of possibilities, thanks to Lua.







# Chapter 8: Making a Dashboard 

Modern web applications greatly rely on client-side JavaScript (JS, also known
 as ECMAScript). Some JS frameworks go all the way in terms of providing a full **Model-View-Controller** (**MVC**) system, which runs in the browser and manipulates the **Document Object Model** (**DOM**), the structured representation of the web page that is rendered in a browser.



现代web应用程序在很大程度上依赖于客户端JavaScript 一些JS框架在提供完整的模型-视图-控制器(MVC)系统方面走了一路，该系统在浏览器中运行，并操作文档对象模型(DOM)，即在浏览器中呈现的web页面的结构化表示。





Tools like Facebook's [ReactJS](https://facebook.github.io/react/) provide high- level APIs to avoid manipulating the DOM directly and offer a level of abstraction which makes client-side web development as comfortable as building Quart applications.

ReactJS 避免直接操作DOM，并提供一个抽象级别，使客户端web开发像构建Quart应用程序一样舒适。



This chapter is composed of the following three parts:

- Building a ReactJS dashboard—a short introduction to ReactJS with an example

- How to embed ReactJS in a Quart app and structure the application

- Authentication and authorization

  





## Building a ReactJS dashboard 

In a similar way to a web server such as nginx, taking care of all the difficult and common parts of the network traffic and leaving you to deal with the logic in your endpoints, ReactJS lets you concentrate on the implementation in your methods instead of worrying about the state of the DOM and the browser. Implementing classes for React can be done in pure JavaScript, or using an extension called JSX. We will discuss JSX in the next section.

类似于web服务器(如nginx)，处理网络流量中所有困难和常见的部分，让你处理端点中的逻辑，ReactJS让你专注于方法中的实现，而不是担心DOM和浏览器的状态。React的类可以用纯JavaScript实现。



### The JSX syntax 

Instead, there is a better, hybrid model using a transpiler – a type of compiler that generates a different form of source code instead of a runnable program. The JSX syntax extension (https://facebook.github.io/jsx/) adds XML tags to JavaScript and can be transpiled into pure JavaScript, either in the browser or beforehand. JSX is promoted by the ReactJS community as the best way to write React apps.



相反，有一种更好的混合模型，使用编译器——一种生成不同形式的源代码而不是可运行程序的编译器。JSX语法扩展(https://facebook.github.io/jsx/)将XML标记添加到JavaScript中，可以在浏览器中或事先将其转换为纯JavaScript。JSX被ReactJS社区推广为编写React应用程序的最佳方式。



### React components 

ReactJS is based on the idea that a web page can be constructed from basic components, which are invoked to render different parts of the display and respond to events such as typing, clicks, and new data appearing.

ReactJS基于这样一种思想，即web页面可以由基本组件构建，这些组件被调用来呈现显示的不同部分，并对键入、单击和新数据出现等事件做出响应。







### Pre-processing JSX 

So far, we have relied on the web browser to convert the JSX files for us. We could still do that, however, it will be the same work being done by each web browser that visits our site. Instead, we can process our own JSX files and provide pure JavaScript to people visiting our site. To do that we must install some tools.

Firstly, we need a JavaScript package manager. The most important one to use is npm (https://www.npmjs.com/). The npm package manager is installed via Node.js. On macOS, the brew install node command does the trick, or you can go to the **Node.js** home page (https://nodejs.org/en/) and download it to the system. Once Node.js and npm are installed, you should be able to call the npm command from the shell as follows:

到目前为止，我们一直依赖web浏览器为我们转换JSX文件。我们仍然可以这样做，但是，这将是由访问我们网站的每个web浏览器所做的相同工作。相反，我们可以处理自己的JSX文件，并为访问我们站点的人提供纯JavaScript。要做到这一点，我们必须安装一些工具。
首先，我们需要一个JavaScript包管理器。最重要的是npm (https://www.npmjs.com/)。npm包管理器是通过Node.js安装的。在macOS上，可以使用brew install node命令，也可以访问node .js主页(https://nodejs.org/en/)并将其下载到系统中。一旦Node.js和npm被安装，你应该能够从shell调用npm命令，如下所示:





## ReactJS and Quart 

From the perspective of the server, the JavaScript code is a static file, and so serving React apps with Quart is no trouble at all. The HTML page can be rendered with Jinja2, and the transpiled JSX files can be provided as static content alongside
 it, much like you would do for plain JavaScript files. We can also get the React distribution and serve those files, or rely on a **Content Delivery Network** (**CDN**) to provide them.

In many cases a CDN is the better option, as retrieving the files will be faster, and the browser then has the option of recognizing that it has already downloaded these files and can use a cached copy to save time and bandwidth. Let's name our Quart application dashboard, and start off with a simple structure like this:

从服务器的角度来看，JavaScript代码是一个静态文件，所以用Quart服务React应用一点问题都没有。HTML页面可以用Jinja2呈现，转译后的JSX文件可以作为静态内容提供
它，就像您对普通JavaScript文件所做的那样。我们还可以获得React分发版并提供这些文件，或者依靠内容交付网络(CDN)来提供这些文件。
在许多情况下，CDN是更好的选择，因为检索文件会更快，然后浏览器可以选择识别它已经下载了这些文件，并可以使用缓存副本来节省时间和带宽。让我们命名我们的Quart应用程序仪表板，并从这样一个简单的结构开始:



基本的quart應用嵌入html像這樣

```python
from quart import Quart,render_template 
app = Quart(__name__)
@app.route("/")
def index():
  return render_template('index.html')

if __name__ =='__main__':
  app.run()
  
```

Thanks to Quart's convention on static assets, all the files contained inside the static/ directory are served under the /static URL. The index.html template looks like the one described in the previous section and can grow into something Quart- specific later on. That is all we need to serve a ReactJS-based app through Quart.

Throughout this section, we have worked on the assumption that the JSON data that React picked was served by the same Quart app. Doing AJAX calls on the same domain is not an issue, but in case you need to call a microservice that belongs
 to another domain, there are a few changes required on both the server and the client side.

由于Quart关于静态资产的约定，静态/目录中包含的所有文件都在/static URL下提供服务。index.html模板类似于前一节中描述的模板，并且可以在以后成长为特定于夸特的模板。这就是我们通过Quart提供一个基于reactjs的应用程序所需要的全部内容。
在本节中，我们假设React选择的JSON数据是由同一个Quart应用程序提供的。在同一个域上执行AJAX调用不是问题，但如果你需要调用属于该域的微服务
对于另一个域，服务器端和客户端都需要进行一些更改。





### Cross-origin resource sharing

Allowing client-side JavaScript to perform cross-domain requests is a potential security risk.

允许客户端JavaScript执行跨域请求是一个潜在的安全风险。





This is why all browsers use the W3C standard for cross-origin resources

這就是為什麼開發者使用W3C標準

除了安全之外，这也是防止某人在他们的web应用程序中使用你的带宽的好方法。例如，如果你在你的网站上提供了一些字体文件，你可能不希望其他网站在他们的页面上使用它们，并在不受任何控制的情况下使用你的带宽。然而，有一些合法的用例想要与其他域共享你的资源，你可以在你的服务上设置规则，允许其他域访问你的资源。





The **Quart-CORS** (https://gitlab.com/pgjones/quart-cors/) project allows us to add support for this very simply:

```python
from quart import Quart 
from quart_cors import cors 

app = Quart(__name__)
app = cors(app,allow_origin='https://quart.com')

@app.route('/api')
async def my_microservice():
    return {"Hello":"World"}

```





## Authentication and authorization认证和授权



The React dashboard needs to be able to authenticate its users and perform authorized calls on some microservices. It also needs to enable the user to grant access to any third-party sites we support, such as Strava or GitHub.

React仪表板需要能够对其用户进行身份验证，并在一些微服务上执行授权调用。它还需要使用户能够授权访问我们支持的任何第三方网站，如Strava或GitHub。





### A note about Micro Frontends 关于Micro frontend的注意事项

This approach introduces some of the same complications that a monolithic backend suffers from. A change to any of the backend or its user interface means updating a microservice and the user interface elements that query it, and those may well be in different source control repositories or managed by different teams. Perhaps support for both the old and new ways has to be introduced for a managed migration, or careful timing with different deployment mechanisms has to happen.

这种方法引入了与单片后端相同的一些并发症。对任何后端或其用户界面的更改都意味着更新一个微服务和查询它的用户界面元素，而这些元素可能在不同的源代码控制存储库中或由不同的团队管理。为了进行托管迁移，可能必须同时引入对旧方法和新方法的支持，或者必须谨慎地选择不同的部署机制。





With all that said, the Micro Frontend model is still relatively new, and many best practices and even bits of terminology are still in flux. For that reason, we shall focus on a simpler variant of this approach and have the authentication service provide its own HTML for logging a user in and creating an account that can be included in an iframe within another page if desired.

综上所述，Micro Frontend模型仍然相对较新，许多最佳实践甚至一些术语仍在不断变化。因此，我们将关注这种方法的一种更简单的变体，并让身份验证服务提供自己的HTML，用于用户登录和创建帐户，如果需要，该帐户可以包含在另一个页面的iframe中。









### Getting the Slack token获取Slack令牌

Slack provides a typical three-legged OAuth2 implementation, using a simple set of HTTP GET requests. Implementing the exchange is done by redirecting the user to Slack and exposing an endpoint the user's browser is redirected to once access has been granted.

Slack提供了一个典型的三足OAuth2实现，使用一组简单的HTTP GET请求。实现交换的方法是将用户重定向到Slack，并公开一个终端，一旦授予访问权限，用户的浏览器就会重定向到这个终端。







### JavaScript authenticationJavaScript验证

When the Dashboard app performs the OAuth2 exchange with Slack, it stores user information in the session, which is a fine approach for the user authenticating on the dashboard. However, when the ReactJS UI calls the DataService microservice to display the user runs, we need to provide an authentication header. The following are two ways to handle this problem:

当Dashboard应用程序与Slack执行OAuth2交换时，它将用户信息存储在会话中，这是用户在仪表板上进行身份验证的好方法。然而，当ReactJS UI调用DataService微服务来显示用户运行时，我们需要提供一个身份验证头。下面有两种方法可以解决这个问题:

- Proxy all the calls to the microservices via the Dashboard web app using the existing session information使用现有的会话信息，通过Dashboard web应用程序代理所有对微服务的调用
- Generate a JWT token for the end user,which can be stored and used against another microservice为最终用户生成一个JWT令牌，该令牌可以存储并用于另一个微服务



# Chapter 9: Packing and Running Python 

 In 1998, Distutils was added to the standard library to provide essential support to create installable distributions for Python projects. 

1998年，Distutils被添加到标准库中，为为Python项目创建可安装的发行版提供必要的支持。



Moreover, developing in such a context can be tedious if you need to reinstall new versions of your microservices all the time. This leads to one question in particular: *how can you correctly install the whole stack in your environment and develop in it?*

此外，如果你需要一直重新安装微服务的新版本，那么在这样的环境下开发会很乏味。这导致了一个特别的问题:如何正确地在您的环境中安装整个堆栈并在其中进行开发?



## The packaging toolchain

 In other words, a change in the standard library takes months to be released, whereas a change in a third-party project can be made available much faster. All third-party projects that are considered as being part of the de facto standard packaging toolchain are now all grouped under the **PyPA** (https://www.pypa.io) umbrella project.



换句话说，标准库中的更改需要几个月的时间才能发布，而第三方项目中的更改可以更快地发布。所有被认为是事实上标准打包工具链的一部分的第三方项目现在都在PyPA (https://www.pypa.io)伞形项目下。



### A few deinitions 

- python package 

  is a directory tree containing Python modules. You can import it, and it is part of the module namespace.

  

- python project 

  can contain several packages, modules, and other resources and is what you release. Each microservice you build with Flask is a Python project.

  

- python application 

  is a Python project that can be directly used through a user interface. The user interface can be a command-line script or a web server.

  

- python library 

   is a specific kind of Python project that provides features to be used in other Python projects and has no direct end-user interface.

  

### Packing 

When you package your python project,there are three standard files you need to have alongside your python packages:当你打包你的python项目时，你需要在你的python包旁边有三个标准文件:

- pyproject.toml: A configuration file or for the project's build system用于项目构建系统的配置文件

- setup.py or setup.cfg: A special module that controls packaging and metadata about the project

  控制关于项目的打包和元数据的特殊模块

   

- requirements.txt:  A file listing dependencies 列出依赖项的文件

  

  

#### The setup.py file 

The setup.py file is what governs everything when you want to interact with a Python project. 

当您希望与Python项目交互时，setup.py文件将管理所有内容。



A common mistake when creating the setup.py file is to import your package into it when you have third-party dependencies. If a tool like pip tries to read the metadata by running setup.py, it might raise an import error before it has a chance to list all the dependencies to install. The only dependency you can afford to import directly in your setup.py file is Setuptools, because you can assume that anyone trying to install your project is likely to have it in their environment.

在创建setup.py文件时，一个常见的错误是当您有第三方依赖关系时将您的包导入其中。如果像pip这样的工具试图通过运行setup.py来读取元数据，它可能会在有机会列出要安装的所有依赖项之前引发导入错误。在setup.py文件中可以直接导入的唯一依赖项是Setuptools，因为您可以假设任何试图安装您的项目的人都可能在他们的环境中拥有它。



If you are missing any critical options, then Setuptools will provide information about the ones it needs when you try to use it. The following is an example of a setup.py file that includes these options:

如果您缺少任何关键选项，那么当您尝试使用它时，Setuptools将提供有关所需选项的信息。下面是一个setup.py文件的示例，其中包含这些选项:

```python
from setuptools import setup,find_packages 

with open('README.rst') as f:
  LONG_DESC = f.read()
setup(
name = 'myProject',
version = '1.0.0',
url = 'http://example.com',
description = 'This is a cool microservice based on Quart',
long_description=LONG_DESC,
long_description_content_type='text/x-rst',
author='danyow',
author_email = 'danyowchueng@gmail.com',
license = 'None',
classifiers = [
  "Development Status :: 3 - Alpha",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3",
],
  keywords = ['quart','microservice'],
  packages = find_packages(),
  include_package_data = True,
  zip_safe = False ,
  install_requires = ['quart'],
)
```



#### The requirements.txt file 

Using this file has been widely adopted by the community, because it makes it easier to document your dependencies. You can create as many requirements files as you want in a project, and have your users call the pip install -r requirements.txt command to install the packages described in them

簡單來說，使用python 項目時候，直接`pip install requirements.txt`就可以完成所有python第三方庫的安裝。





To summarize, defining dependencies should be done in each project's setup.py file, and requirements files can be provided with pinned dependencies if you have a reproducible process to generate them from the setup.py file to avoid duplication.

总而言之，定义依赖关系应该在每个项目的setup.py文件中完成，如果您有一个可重复的过程来从setup.py文件中生成需求文件以避免重复，则可以为需求文件提供固定的依赖关系。





#### The MANIFEST.in file 

When creating a source or binary release, Setuptools will include all the package modules and data files, the setup.py file, and a few other files automatically in the package archive. Files like pip requirements will not be included. To add them to your distribution, you need to add a MANIFEST.in file, which contains the list of files to include.

当创建源代码或二进制版本时，Setuptools将包含所有的包模块和数据文件、setup.py文件以及包归档中自动包含的其他一些文件。像pip要求这样的文件将不包括在内。要将它们添加到您的发行版中，您需要添加一个MANIFEST。文件中，其中包含要包含的文件列表。



The file follows a simple glob-like syntax, described at the following, where you refer to a file or a directory pattern and say whether you want to include or prune the matches: https://docs.python.org/3/distutils/commandref.html#creating-a- source-distribution-the-sdist-command.

Here's an example from Jeeves:

该文件遵循一个简单的类似glob的语法，如下所述，其中您引用一个文件或目录模式，并表示您是想包含还是删除匹配项:https://docs.python.org/3/distutils/commandref.html#creating-a- source-distribution- The -sdist-命令。
下面是来自Jeeves的一个例子:

`include requirements.txt`

`include README.rst`

`include LINCENSE`

`recursive-include myservice *.ini`

`recursive-include docs *.rst *.png *.svg *.css *.html conf.py`

`prune docs/build/*`

 A typical microservice project, as described in this book, will have the following list of files:

一个典型的微服务项目，如本书所述，将有以下文件列表:

- setup.py 
- README.rst 
- MANIFEST.in :
- A code of conduct,if the code is an open-source project 
- requirements.txt :pip requirement files generated from install_requires
- docs/: The Sphinx documentation
- A directory containing the microservice code,which will typically be named after the microservice,or src/







### Versioning 版本控制

介紹了0.x.0差別版本

正式出版版本號應該為1.0.0



### Releasing 發佈版本

To release your project, we must build a package that can be either uploaded to a package repository such as PyPI or installed directly wherever it is needed. Python has a build utility that makes this process straightforward.

为了发布您的项目，我们必须构建一个包，该包可以上传到诸如PyPI这样的包存储库，也可以直接安装在任何需要的地方。Python有一个构建实用程序，可以使这个过程变得简单。

In the following example, we install the build utility, and then run it in the example project we used earlier in this chapter. The output can be quite long, so only some of it is included below:在下面的示例中，我们安装构建实用程序，然后在本章前面使用的示例项目中运行它。输出可能会很长，所以下面只包括部分输出:

```python
!pip install --upgrade build

python -m build 

```

the build command reads the information from setup.py and MANIFEST.in collects all the files ,and put them in an archive,the result is created in the dist directory

```powershell
ls dist/
```


请注意，存档的名称由项目名称及其版本组成。归档文件采用Wheel格式，在PEP 427中定义，这是目前分发Python包的最佳格式，尽管过去有不同的方法，您可能会在现有项目中遇到。这个存档可以直接使用pip来安装项目，如下所示:
```powershell
pip install dist/xxxx.whl

```


## Running all microservice 

pass



## Process management 





# Chapter 10: Deploying on AWS 

> 最重要的章节

**Virtual Machines** (**VMs**) can be a good solution, as they provide an isolated environment in which to run your code





The big revolution came with **Docker**, an open-source virtualization tool first released in 2013. Docker allows the use of isolated environments called *containers* to run applications in a very portable way.

最大的变革来自于2013年首次发布的开源虚拟化工具Docker。Docker允许使用被称为容器的隔离环境以一种非常可移植的方式运行应用程序。





## What is Docker

The Docker project is a container platform,which lets you run your applications in isolated environments.Using the Linux feature called cgroups,

Docker项目是一个容器平台，它允许您在隔离的环境中运行应用程序。使用名为cgroups的Linux特性，

Docker creates isolated environments called containers that run on Linux without a VM. On macOS and Windows, installing Docker will create a lightweight VM for you to run containers in, although this is a seamless process. This means that macOS, Windows, and Linux users can all develop container-based applications without worrying about any interoperability trouble and deploy them to a Linux server where they will run natively.

Docker创建隔离的环境，称为容器，在Linux上运行，不需要虚拟机。在macOS和Windows上，安装Docker将为你创建一个轻量级的虚拟机来运行容器，尽管这是一个无缝的过程。这意味着macOS、Windows和Linux用户都可以开发基于容器的应用程序，而不用担心任何互操作性问题，并将它们部署到Linux服务器上，在那里它们将本机运行。





检查有无安装docker的终端命令为

`docker version`



## Introduction to Docker

Let's experiment with Docker containers. Running a container that you can enter commands in is as simple as the following:

`docker run -- ineractive --tty ubuntu:20.04 bash`

With this command, we are telling Docker to run the Ubuntu image, which will be fetched from Docker Hub, a central registry of public images. We are providing a tag of 20.04 after the image name so that we download the container image that represents the Ubuntu 20.04 operating system. This won't contain everything that a regular Ubuntu installation has, but anything that's missing is installable.

通过这个命令，我们告诉Docker运行Ubuntu映像，该映像将从Docker Hub(一个公共映像的中央注册中心)获取。我们在映像名称后面提供了一个20.04标记，以便下载代表Ubuntu 20.04操作系统的容器映像。它不会包含常规Ubuntu安装的所有内容，但任何缺少的内容都是可以安装的。

The standard name for these Docker configuration files is a Dockerfile, and the following is a basic example of one:

<u>这些Docker配置文件的标准名称是Dockerfile</u>，下面是一个基本的例子:

`FROM ubuntu:20.04`

`RUN apt-get update && apt-get install -y python3`

`CMD['bash']`

A Dockerfile is a text file with a set of instructions. Each line starts with the instruction in uppercase, followed by its arguments. In our example, there are these three instructions:

Dockerfile是一个带有一组指令的文本文件。每行以大写的指令开始，后面跟着它的参数。在我们的例子中，有三个指令:



- FROM: Points to the base image to use指针应用哪一个操作系统

- RUN: Runs the commands in the container once the base image is installed

  一旦安装了基本映像，就在容器中运行命令

  

- CMD: The command to run when the container is executed by Docker

  Docker在容器执行时执行的命令

to use python3.9 from the alpine base image, you can create a Dockerfile like this:

`FROM python3.0-alpine CMD['python3.9']`



## Running Quart in Docker

In the following example, we introduce the COPY command, which will recursively copy files and directories from outside the container into the image. We also add the EXPOSE directive to indicate to anyone running the container that this port should be exposed to the outside world. We still need to connect that exposed port when we run the container with the -p option. Any process inside the container can listen to any ports that it wants to, and communicate with itself using localhost, but anything outside the container won't be able to reach the inside unless that port has been exposed. It's also worth noting that localhost inside the container only refers to the container, not the computer that's hosting the running containers; so, if you need to communicate with other services, you will need to use its real IP address:

在下面的示例中，我们将引入COPY命令，该命令将递归地将容器外部的文件和目录复制到映像中。我们还添加了EXPOSE指令，向运行容器的任何人指示，应该将这个端口暴露给外部世界。在使用-p选项运行容器时，我们仍然需要连接那个暴露的端口。容器内的任何进程都可以侦听它想侦听的任何端口，并使用localhost与自己通信，但容器外的任何进程都无法到达容器内部，除非该端口已公开。同样值得注意的是，容器内部的localhost只指向容器本身，而不是承载运行容器的计算机;所以，如果你需要与其他服务通信，你需要使用它的真实IP地址:

```
FROM python:3.9
COPY . /app/
RUN pip install -r /app/requirements.txt
RUN pip install /app/
CMD ["hypercorn", "—bind", "0.0.0.0:5000", "myservice:app"]
```









## Docker-based deployments 

这一步还是没有aws，visa的信用卡

无法实现



### Terraform

Before we head further into the different container orchestration tools, it's worth mentioning a different sort of tool that can organize the underlying cloud instances. **Terraform**, made by the company HashiCorp, is a widely adopted tool for defining resources as code. 

在进一步讨论不同的容器编排工具之前，有必要介绍一种不同类型的工具，它可以组织底层云实例。由HashiCorp公司开发的Terraform是一种被广泛采用的将资源定义为代码的工具。



### Service discovery

We very quickly come across scenarios that complicate a static configuration. If we need to move a microservice to a new AWS region, or a different cloud provider entirely, then how do we tell all the other microservices that use it? If we add a new feature that's controlled by a feature flag, how do we quickly turn it on and off? On a smaller scale, how does a load balancer know about all the containers that should receive traffic?

我们很快就会遇到使静态配置复杂化的场景。如果我们需要将一个微服务移动到一个新的AWS区域，或者完全不同的云提供商，那么我们如何告知所有使用它的其他微服务?如果我们添加一个由特性标志控制的新特性，我们如何快速地打开和关闭它?在较小的范围内，负载均衡器如何知道应该接收流量的所有容器?





We will use etcd as an example, with a basic Quart service, while also utilizing the etcd3 Python library. Assuming you have etcd running with the default options after following the instructions on their website, we can add some configuration- updating code to our service, and have an endpoint that returns the URL we would contact, if the application was more complete:

我们将以etcd为例，使用一个基本的Quart服务，同时还使用etcd3 Python库。假设你按照etcd网站上的说明运行了默认选项，我们可以在我们的服务中添加一些配置更新代码，并有一个端点返回我们将联系的URL，如果应用程序更完整的话:

```python
from quart import Quart,current_app 
import etcd3 

# can read this map from a tranditional config file
setting_map ={
    'dataset_url':'/services/dataservice/url'
}

setting_reverse_map = {v:k for k,v in setting_map.items()}

etcd_client = etcd3.client()
def load_settings():
    config = dict()
    for setting,etcd_key in setting_map.items():
        config[setting] = etcd_client.get(etcd_key)[0].decode('utf-8')
    return config

def create_app(name=__name__):
    app = Quart(__name__)
    app.config.update(load_settings())
    return app 

def watch_callback(event):
    global app 
    for update in event.events:
        # determine which settings to update,and convert from bytes to str 
        config_option = setting_reverse_map[update.key.decode('utf-8')]
        app.config[config_option] = update.value.decode('utf-8')

# start to watch for dataservice url changes 
# you can also watch entire areas with add_watch_prefix_callback
watch_id = etcd_client.add_watch_callback('/services/dataservice/url')
watch_callback()

@app.route('/api')
def what_is_url():
    return {"url":app.config['dataservice_url']}
app.run()

```



### Docker Compose Docker组成

 Docker Compose (https://docs.docker.com/compose/) simplifies the task by letting you define multiple containers' configuration in a single configuration file, as well as how those containers depend on each other. 

Docker Compose (https://docs.docker.com/compose/)允许你在一个配置文件中定义多个容器的配置，以及这些容器如何相互依赖，从而简化了这一任务。

Once the script is installed on your system, create a yaml file containing the information about services and networks that you want to run. The default filename is docker-compose.yml, and so we will use that name for our examples to make the commands simpler.

在系统上安装脚本之后，创建一个yaml文件，其中包含关于您想要运行的服务和网络的信息。默认文件名是docker-compose。Yml，因此我们将在示例中使用这个名称，以使命令更简单。



### Docker Swarm Docker群

Docker has a built-in cluster functionality called **swarm** mode (https://docs. docker.com/engine/swarm/). This mode has an impressive list of features, which lets you manage all your container clusters from a single utility. This makes it ideal for smaller deployments or ones that do not need to scale up and down as flexibly to meet changing demands.

Docker有一个内置的集群功能，叫做**swarm**模式(https://docs。docker.com/engine/swarm/)。此模式具有令人印象深刻的特性列表，允许您从一个实用程序管理所有容器集群。这使得它非常适合小型部署或不需要灵活伸缩以满足不断变化的需求的部署。





## Kubernetes

Originally designed by Google, but now maintained by an independent foundation, **Kubernetes** (https://kubernetes.io/, also known as k8s) provides a platform- independent way of automating work with containerized systems, allowing you to describe the system in terms of different components, and issuing commands to a controller to adjust settings.

最初由谷歌设计，但现在由Kubernetes (https://kubernetes)独立基金会维护。Io /(也称为k8s)提供了一种独立于平台的方式来自动化容器化系统的工作，允许您根据不同的组件来描述系统，并向控制器发出命令来调整设置。



Rather than create all the AWS resources yourself, or create Terraform configuration to do so, eksctl performs all the work for you, with sensible defaults for experimenting with Kubernetes. To get started, it is best to use the AWS credentials we created for earlier examples and to install both eksctl and kubectl—the Kubernetes command line. The AWS credentials will be used by eksctl to create the cluster and other necessary resources, and once done, kubectl can be used to deploy services and software. Unlike Docker Swarm, kubectl's administrative commands are designed to be run from your own computer:

与自己创建所有AWS资源或创建terrraform配置不同，eksctl为您执行所有工作，并使用合理的默认值来试验Kubernetes。首先，最好使用我们为前面的示例创建的AWS凭据，并同时安装eksctl和kubectl—Kubernetes命令行。eksctl将使用AWS凭证创建集群和其他必要的资源，完成后，kubectl可用于部署服务和软件。与Docker Swarm不同，kubectl的管理命令被设计成可以在你自己的计算机上运行:



## Summary 

As a guide, consider:

- Docker Compose when you need to deploy multiple containers in a small environment, and do not need to manage a large infrastructure.
- Docker Swarm when you need flexibility in how many containers are deployed, to respond to a changing situation, and are happy to manage a larger cloud infrastructure.
- Kubernetes when automation and flexibility are paramount, and you have people and time available to manage the infrastructure and handle the complexity.





You will not be locked into one orchestration tool once you choose it, as the containers you build can be used in any of them, but moving to a different orchestration tool can be hard work, depending on how complex your configuration is.

In that vein, to make their services easier to use and more appealing, cloud providers have built-in features to handle deployments. The three largest cloud providers are currently AWS, Google Cloud, and Microsoft Azure, although many other good options exist.



作为指导，考虑:

- Docker Compose:当你需要在一个小环境中部署多个容器，而不需要管理大型基础设施时。

- Docker Swarm，当你需要灵活部署多少容器，以响应不断变化的情况，并乐于管理更大的云基础设施。
-
- 当自动化和灵活性是最重要的，你有人力和时间来管理基础设施和处理复杂性时，Kubernetes。

一旦选择了某个编排工具，您就不会被锁定在该工具中，因为您构建的容器可以在任何一个编排工具中使用，但是迁移到不同的编排工具可能是一项艰巨的工作，这取决于您的配置有多复杂。

在这种情况下，为了使他们的服务更容易使用和更有吸引力，云提供商有内置的功能来处理部署。目前最大的三个云提供商是AWS、谷歌cloud和Microsoft Azure，尽管还有许多其他好的选择。



