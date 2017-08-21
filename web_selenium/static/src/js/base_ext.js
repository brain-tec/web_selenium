odoo.define('web_selenium.base_ext', function(require){
  "option strict";
  
  var KanbanRecord = require('web_kanban.Record');
  
  var kanban_record = KanbanRecord.include({
    renderElement: function() {
      this._super.apply(this, arguments);
      this.$el.attr('data-bt-testing-model_name', this.model);
      this.$el.attr('data-bt-testing-name', this.record && this.record.name && this.record.name.raw_value);
    }
  });
  
  return {
    KanbanRecord: kanban_record
  };
});