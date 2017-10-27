odoo.define('web_selenium.base_ext', function(require){
  "option strict";

  // tested: ok 11.0EE
  var Widget = require('web.Widget');
  Widget.include({
    addSeleniumData: function() {
      this.$el.attr('data-bt-testing-model_name', this.modelName || this.model || this.env.modelName);
      this.$el.attr('data-bt-testing-name', this.record && this.record.name && this.record.name.raw_value || this.name || this.title);
    }
  });

  // tested: ok 11.0EE
  var AbstractField = require('web.AbstractField');
  AbstractField.include({
    start: function() {
      return this._super.apply(this, arguments).then(this.addSeleniumData.bind(this));
    }
  });

  // tested: ok 11.0EE
  var FieldSelection = require('web.relational_fields').FieldSelection;
  FieldSelection.include({
    _renderEdit: function () {
      this._super.apply(this, arguments);
      var widget = this;
      this.$el.find('option').each(function() {
        $el = $(this);
        $el.attr('data-type', widget.field && widget.field.type);
        // When the field is selection, take the technical value so to stay language independent. 
        // If it is a many2one field, take the name of the field instead of the id.
        // It's better to be database independent than language independent
        $el.attr('data-bt-testing-value', widget.field && widget.field.type === 'many2one' ? $el.text() : $el.val());
      });
    }
  });

  // tested: ok 11.0EE
  var KanbanRecord = require('web.KanbanRecord');
  KanbanRecord.include({
    start: function() {
      return this._super.apply(this, arguments).then(this.addSeleniumData.bind(this));
    }
  });

  // tested: ok 11.0EE
  var ListRenderer = require('web.ListRenderer');
  ListRenderer.include({
    _renderRow: function(record) {
      var $el = this._super.apply(this, arguments);
      $el.attr('data-bt-testing-model_name', record.model);
      return $el;
    }
  });

  // tested: ok 11.0EE
  var FormRenderer = require('web.FormRenderer');
  FormRenderer.include({
    _renderTabHeader: function() {
      var $el = this._super.apply(this, arguments);
      this._addModelDataToElement($el.find('a'));
      return $el;
    },

    _renderHeaderButton: function() {
      var $el = this._super.apply(this, arguments);
      this._addModelDataToElement($el);
      $el.attr('type_data_is', 'WidgetButton');
      return $el;
    },

    _addModelDataToElement: function(element) {
      element.attr('data-bt-testing-model_name', this.state.model);
    }
  });

  // tested: ok 11.0EE
  var Dialog = require('web.Dialog');
  Dialog.include({
    set_buttons: function() {
      this._super.apply(this, arguments);
      this.$footer.find('button').attr('data-bt-testing-model_name', this.dataset.model);
    }
  });

  // tested: ok 11.0EE
  var ViewManager = require('web.ViewManager');
  ViewManager.include({
    start: function() {
      var self = this;
      return this._super.apply(this, arguments).then(this.addSeleniumData.bind(this));
    }
  });

});
