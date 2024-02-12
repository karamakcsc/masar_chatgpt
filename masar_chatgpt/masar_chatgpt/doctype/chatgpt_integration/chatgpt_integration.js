frappe.ui.form.on("ChatGPT Integration", {
    refresh: function (frm) {
        // Your code here
    },
    execute: function (frm) {
        frappe.call({
            method: "masar_chatgpt.masar_chatgpt.doctype.chatgpt_integration.chatgpt_integration.integration",
            args: {
                user_input: frm.doc.input,
                model: frm.doc.model,
                image: frm.doc.file
            },
            callback: function (r) {
                if(frm.doc.model=="gpt-4"||frm.doc.model=="gpt-4-32k"||frm.doc.model =="gpt-3.5-turbo-0125"||frm.doc.model == "gpt-3.5-turbo-instruct"){
                    frm.set_value('chatgpt_answer', r.message);
                }else if(frm.doc.model == "dall-e-3"){
                    frm.set_value('url_image', r.message)
                }
                
                
            }
        });
    }
});
