frappe.pages['chat-integration'].on_page_load = function (wrapper) {
	new MyPage(wrapper);
 }
 
 class MyPage {
	constructor(wrapper) {
	   this.page = frappe.ui.make_app_page({
		  parent: wrapper,
		  title: 'Chat Integration',
		  single_column: true
	   });
	   this.make();
	}
 
	make() {
	   const body = `
		  <div class="chat-container">
			 <div class="chat-history" id="chat-history"></div>
			 <input type="text" id="user-input" />
			 <button onclick="sendMessage()">Send</button>
		  </div>
		  <script>
			 function sendMessage() {
				var userInput = document.getElementById("user-input").value;
				frappe.call({
				   method: "masar_chatgpt.api.get_chat_response",
				   args: { "user_input": userInput },
				   callback: function (r) {
					  document.getElementById("chat-history").innerHTML += "<p>User: " + userInput + "</p>";
					  document.getElementById("chat-history").innerHTML += "<p>ChatGPT: " + r.message + "</p>";
				   }
				});
			 }
		  </script>
	   `;
	   $(body).appendTo(this.page.main);
	}
 }
 