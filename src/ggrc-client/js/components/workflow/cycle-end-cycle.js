/*
  Copyright (C) 2019 Google Inc.
  Licensed under http://www.apache.org/licenses/LICENSE-2.0 <see LICENSE file>
*/

import {
  getPageInstance,
} from '../../plugins/utils/current-page-utils';
import {initCounts} from '../../plugins/utils/widgets-utils';
import {countsMap as workflowCountsMap} from '../../apps/workflows';
import {trigger} from 'can-event';

/**
 * A component that wraps a button for ending a Workflow cycle, and
 * automatically handles a click on it.
 *
 * As a result, the Cycle instance passed to the component is ended, and
 * a couple of affected objects are refreshed in the process.
 *
 * Usage example (state and permission checks not included):
 *
 *   <cycle-end-cycle cycle:from="instance">
 *       <button>Click to end a Cycle</button>
 *   </cycle-end-cycle>
 *
 */

export default can.Component.extend({
  tag: 'cycle-end-cycle',
  viewModel: can.Map.extend({
    cycle: null,
  }),
  events: {
    click: function (el, ev) {
      ev.stopPropagation();

      this.viewModel.attr('cycle')
        .refresh()
        .then(function (cycle) {
          return cycle.attr('is_current', false).save();
        })
        .then(function () {
          return getPageInstance().refresh();
        })
        .then(function () {
          let pageInstance = getPageInstance();
          trigger.call(el[0], 'refreshTree');

          return initCounts(
            [workflowCountsMap.history],
            pageInstance.type,
            pageInstance.id);
        });
    },
  },
  leakScope: true,
});