$(function() {
  var instance = openerp;

  instance.web.form.FieldMany2Many.include({
    initialize_content: function() {
      this.$el.attr('data-bt-testing-model_name', this.view && this.view.fields_view.model);
      this.$el.attr('data-bt-testing-name', this.name);
      this.$el.attr('data-bt-testing-submodel_name', this.dataset && this.dataset.model);
      this._super.apply(this, arguments);
    }
  });

  instance.web.UserMenu.include({
    do_update: function() {
      var el = this.$el.find('.oe_topbar_name')
      el.attr('data-bt-testing-session_username', this.session.username);
      this._super.apply(this, arguments);
    }
  });
});